import re
from typing import Dict, List, Set, Tuple

from shapely.geometry import LineString, Polygon

from apollo.utils import calculate_velocity, generate_adc_polygon
from config import HD_MAP
from framework.oracles.OracleInterface import OracleInterface
from hdmap.MapParser import MapParser
from modules.localization.proto.localization_pb2 import LocalizationEstimate
from modules.planning.proto.decision_pb2 import STOP_REASON_STOP_SIGN
from modules.planning.proto.planning_pb2 import ADCTrajectory


class StopSignOracle(OracleInterface):
    """
    The Stop Sign Oracle is responsible for checking if the ADS instance made a complete
    stop before crossing a stop line controlled by a stop sign. After the oracle detects
    the ADS instance crossing a stop line, it looks backward to check if the ADS stopped
    for stop sign by looking at its main planning decision and its speed trace.
    """

    past_localization_list: List[LocalizationEstimate]
    past_planning_list: List[ADCTrajectory]

    violated_at_stop_sign_ids: Set[str]
    stop_sign_stop_line_string_dict: Dict[str, LineString]

    ADC_INTERSECTING_STOP_LINE_MAX_LOOK_BACK_FRAMES_IN_SECOND = 5.0

    # Apollo: virtual_obstacle_id = STOP_SIGN_VO_ID_PREFIX + stop_sign_overlap.object_id;
    STOP_SIGN_VO_ID_PREFIX = "SS_"

    checked: Set

    def __init__(self):
        self.violated_at_stop_sign_ids = set()

        self.parse_stop_sign_stop_line_string_on_map(MapParser.get_instance(HD_MAP))
        self.reset_all_oracle_states()
        self.checked = set()

    def get_interested_topics(self):
        """
        The stop sign oracle is interested in Planning messages and Localization messages.
        Localization messages are used to check if the AV is crossing a stop line,
        and check if the AV's speed reached 0.0 m/s. Planning messages are used to check
        if the AV's main decision was indeed for the stop sign, not stopping for other reasons
        (e.g., obstacle)
        """
        return [
            '/apollo/localization/pose',
            '/apollo/planning',
        ]

    def on_new_message(self, topic: str, message, t):
        """
        Upon receiving a planning/localization message, this oracle may not perform any
        analysis if the AV is not crossing any stop line. Once the oracle detects it is
        crossing a stop line, it looks at messages cached and analyze whether the AV
        stopped for the stop sign before crossing the stop line.

        :param str topic: topic of the message
        :param any message: either Planning or Localization message
        :param float t: the timestamp
        """
        self.prune_old_messages()

        if topic == '/apollo/localization/pose':
            self.past_localization_list.append(message)
        else:
            self.past_planning_list.append(message)
            return

        if not self.past_localization_list or not self.past_planning_list:
            return

        crossing_stop_sign_id = self.check_if_adc_intersecting_any_stop_lines()

        if crossing_stop_sign_id == "" or crossing_stop_sign_id in self.checked:
            return

        # when ADC started intersecting, check if stop decision was made before that
        self.checked.add(crossing_stop_sign_id)

        # the code below means that ADC just crossed the stop line
        # while in the previous message it was still intersecting the stop_line
        # -> now we will check if ADC actually
        # (1) made STOP decision, and
        # (2) completely stopped (reaches 0.0 m/s) before crossed the stop line

        is_adc_followed_stop_sign_rule = False
        last_localization_timestamp = self.past_localization_list[-1].header.timestamp_sec
        for past_localization in self.past_localization_list[::-1]:
            past_localization_timestamp = past_localization.header.timestamp_sec
            if last_localization_timestamp - past_localization_timestamp > self.ADC_INTERSECTING_STOP_LINE_MAX_LOOK_BACK_FRAMES_IN_SECOND:
                break

            # check condition (2)
            if not self.was_adc_completely_stopped(past_localization):
                continue

            # check condition (1)
            for past_planning in self.past_planning_list[::-1]:
                past_planning_timestamp = past_planning.header.timestamp_sec
                # get 1 planning message just before this localization message
                if past_planning_timestamp > past_localization_timestamp:
                    continue
                if self.is_planning_main_decision_to_stop_at_stop_sign(past_planning, crossing_stop_sign_id):
                    is_adc_followed_stop_sign_rule = True
                break

            if is_adc_followed_stop_sign_rule:
                break

        if not is_adc_followed_stop_sign_rule:
            self.violated_at_stop_sign_ids.add(crossing_stop_sign_id)

        self.reset_all_oracle_states()

    def get_result(self) -> List[Tuple]:
        """
        Returns a list of violations from this oracle
        """
        result = list()
        for stop_sign_id in self.violated_at_stop_sign_ids:
            violation = ('stop_sign', stop_sign_id)
            result.append(violation)
        return result

    def parse_stop_sign_stop_line_string_on_map(self, map_parser: MapParser) -> None:
        """
        Parse and store stop line for every stop sign on the map

        :param MapParser map_parser: the MapParser singleton instance
        """
        self.stop_sign_stop_line_string_dict = dict()
        stop_sign_ids = map_parser.get_stop_signs()
        for ss_id in stop_sign_ids:
            stop_sign_data = map_parser.get_stop_sign_by_id(ss_id)
            line = LineString(
                [[p.x, p.y] for p in stop_sign_data.stop_line[0].segment[0].line_segment.point])
            self.stop_sign_stop_line_string_dict[ss_id] = line

    def reset_all_oracle_states(self) -> None:
        """
        Resets all oracle states
        """
        self.past_localization_list = list()
        self.past_planning_list = list()

    def check_if_adc_intersecting_any_stop_lines(self) -> str:
        """
        Check if the AV is intersecting any stop line

        :returns: the ID of the stop line intersecting with, or empty string
        :rtype: str
        """
        last_localization = self.past_localization_list[-1]
        adc_pose = last_localization.pose

        adc_polygon_pts = generate_adc_polygon(
            adc_pose.position, adc_pose.heading)
        adc_polygon = Polygon([[x.x, x.y] for x in adc_polygon_pts])
        for stop_sign_id, stop_line_string in self.stop_sign_stop_line_string_dict.items():
            if not stop_line_string.intersection(adc_polygon).is_empty:
                return stop_sign_id
        return ""

    def is_planning_main_decision_to_stop_at_stop_sign(self, planning_message: ADCTrajectory,
                                                       stop_sign_id: str) -> bool:
        """
        Given a planning message, check if its main decision is to stop for stop sign

        :returns: True if includes a stop sign stop decision, False otherwise
        :rtype: bool
        """
        try:
            stop_decision = planning_message.decision.main_decision.stop
        except AttributeError:
            return False

        stop_reason_code = stop_decision.reason_code
        if stop_reason_code != STOP_REASON_STOP_SIGN:
            return False

        # e.g,  stop_reason = "stop by SS_stop_sign_0" (included stop_sign_id)
        stop_reason = stop_decision.reason
        if re.sub("^stop by ", "", stop_reason) == self.STOP_SIGN_VO_ID_PREFIX + stop_sign_id:
            return True

        return False

    @staticmethod
    def was_adc_completely_stopped(past_localization) -> bool:
        """
        Given a localization message, check if the AV completely stopped

        :returns: True if completely stopped, False otherwise
        :rtype: bool
        """
        adc_pose = past_localization.pose
        adc_velocity = calculate_velocity(adc_pose.linear_velocity)

        # https://github.com/ApolloAuto/apollo/blob/0789b7ea1e1356dde444452ab21b51854781e304/modules/planning/scenarios/stop_sign/unprotected/stage_pre_stop.cc#L237
        # return adc_velocity <= self.MAX_ABS_SPEED_WHEN_STOPPED
        return adc_velocity == 0

    def prune_old_messages(self) -> None:
        """
        Remove messages that are too old, i.e., only keep the last 200 messages for analyzing
        """
        total_localization_message_number = len(self.past_localization_list)
        if total_localization_message_number > 200:
            # based on PERCEPTION_FREQUENCY = 25 == 125 messages sent per 5 seconds
            self.past_localization_list = self.past_localization_list[1:]

        total_planning_message_number = len(self.past_planning_list)
        if total_planning_message_number > 200:
            self.past_planning_list = self.past_planning_list[1:]
