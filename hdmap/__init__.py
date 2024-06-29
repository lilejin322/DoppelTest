import sys
from config import APOLLO_ROOT
sys.path.append(APOLLO_ROOT)
from modules.common_msgs.map_msgs.map_pb2 import Map


def load_hd_map(filename: str):
    map = Map()
    f = open(filename, 'rb')
    map.ParseFromString(f.read())
    f.close()
    return map
