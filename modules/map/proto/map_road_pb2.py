# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: modules/map/proto/map_road.proto

import sys

_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from modules.map.proto import \
    map_geometry_pb2 as modules_dot_map_dot_proto_dot_map__geometry__pb2
from modules.map.proto import \
    map_id_pb2 as modules_dot_map_dot_proto_dot_map__id__pb2

DESCRIPTOR = _descriptor.FileDescriptor(
  name='modules/map/proto/map_road.proto',
  package='apollo.hdmap',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n modules/map/proto/map_road.proto\x12\x0c\x61pollo.hdmap\x1a$modules/map/proto/map_geometry.proto\x1a\x1emodules/map/proto/map_id.proto\"\xa9\x01\n\x0c\x42oundaryEdge\x12\"\n\x05\x63urve\x18\x01 \x01(\x0b\x32\x13.apollo.hdmap.Curve\x12-\n\x04type\x18\x02 \x01(\x0e\x32\x1f.apollo.hdmap.BoundaryEdge.Type\"F\n\x04Type\x12\x0b\n\x07UNKNOWN\x10\x00\x12\n\n\x06NORMAL\x10\x01\x12\x11\n\rLEFT_BOUNDARY\x10\x02\x12\x12\n\x0eRIGHT_BOUNDARY\x10\x03\";\n\x0f\x42oundaryPolygon\x12(\n\x04\x65\x64ge\x18\x01 \x03(\x0b\x32\x1a.apollo.hdmap.BoundaryEdge\"q\n\x0cRoadBoundary\x12\x34\n\router_polygon\x18\x01 \x01(\x0b\x32\x1d.apollo.hdmap.BoundaryPolygon\x12+\n\x04hole\x18\x02 \x03(\x0b\x32\x1d.apollo.hdmap.BoundaryPolygon\"d\n\x0fRoadROIBoundary\x12\x1c\n\x02id\x18\x01 \x01(\x0b\x32\x10.apollo.hdmap.Id\x12\x33\n\x0froad_boundaries\x18\x02 \x03(\x0b\x32\x1a.apollo.hdmap.RoadBoundary\"|\n\x0bRoadSection\x12\x1c\n\x02id\x18\x01 \x01(\x0b\x32\x10.apollo.hdmap.Id\x12!\n\x07lane_id\x18\x02 \x03(\x0b\x32\x10.apollo.hdmap.Id\x12,\n\x08\x62oundary\x18\x03 \x01(\x0b\x32\x1a.apollo.hdmap.RoadBoundary\"\xd9\x01\n\x04Road\x12\x1c\n\x02id\x18\x01 \x01(\x0b\x32\x10.apollo.hdmap.Id\x12*\n\x07section\x18\x02 \x03(\x0b\x32\x19.apollo.hdmap.RoadSection\x12%\n\x0bjunction_id\x18\x03 \x01(\x0b\x32\x10.apollo.hdmap.Id\x12%\n\x04type\x18\x04 \x01(\x0e\x32\x17.apollo.hdmap.Road.Type\"9\n\x04Type\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0b\n\x07HIGHWAY\x10\x01\x12\r\n\tCITY_ROAD\x10\x02\x12\x08\n\x04PARK\x10\x03')
  ,
  dependencies=[modules_dot_map_dot_proto_dot_map__geometry__pb2.DESCRIPTOR,modules_dot_map_dot_proto_dot_map__id__pb2.DESCRIPTOR,])



_BOUNDARYEDGE_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='apollo.hdmap.BoundaryEdge.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NORMAL', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LEFT_BOUNDARY', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RIGHT_BOUNDARY', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=220,
  serialized_end=290,
)
_sym_db.RegisterEnumDescriptor(_BOUNDARYEDGE_TYPE)

_ROAD_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='apollo.hdmap.Road.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HIGHWAY', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CITY_ROAD', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PARK', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=857,
  serialized_end=914,
)
_sym_db.RegisterEnumDescriptor(_ROAD_TYPE)


_BOUNDARYEDGE = _descriptor.Descriptor(
  name='BoundaryEdge',
  full_name='apollo.hdmap.BoundaryEdge',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='curve', full_name='apollo.hdmap.BoundaryEdge.curve', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='apollo.hdmap.BoundaryEdge.type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _BOUNDARYEDGE_TYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=121,
  serialized_end=290,
)


_BOUNDARYPOLYGON = _descriptor.Descriptor(
  name='BoundaryPolygon',
  full_name='apollo.hdmap.BoundaryPolygon',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='edge', full_name='apollo.hdmap.BoundaryPolygon.edge', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=292,
  serialized_end=351,
)


_ROADBOUNDARY = _descriptor.Descriptor(
  name='RoadBoundary',
  full_name='apollo.hdmap.RoadBoundary',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='outer_polygon', full_name='apollo.hdmap.RoadBoundary.outer_polygon', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hole', full_name='apollo.hdmap.RoadBoundary.hole', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=353,
  serialized_end=466,
)


_ROADROIBOUNDARY = _descriptor.Descriptor(
  name='RoadROIBoundary',
  full_name='apollo.hdmap.RoadROIBoundary',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='apollo.hdmap.RoadROIBoundary.id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='road_boundaries', full_name='apollo.hdmap.RoadROIBoundary.road_boundaries', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=468,
  serialized_end=568,
)


_ROADSECTION = _descriptor.Descriptor(
  name='RoadSection',
  full_name='apollo.hdmap.RoadSection',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='apollo.hdmap.RoadSection.id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lane_id', full_name='apollo.hdmap.RoadSection.lane_id', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='boundary', full_name='apollo.hdmap.RoadSection.boundary', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=570,
  serialized_end=694,
)


_ROAD = _descriptor.Descriptor(
  name='Road',
  full_name='apollo.hdmap.Road',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='apollo.hdmap.Road.id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='section', full_name='apollo.hdmap.Road.section', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='junction_id', full_name='apollo.hdmap.Road.junction_id', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='apollo.hdmap.Road.type', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _ROAD_TYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=697,
  serialized_end=914,
)

_BOUNDARYEDGE.fields_by_name['curve'].message_type = modules_dot_map_dot_proto_dot_map__geometry__pb2._CURVE
_BOUNDARYEDGE.fields_by_name['type'].enum_type = _BOUNDARYEDGE_TYPE
_BOUNDARYEDGE_TYPE.containing_type = _BOUNDARYEDGE
_BOUNDARYPOLYGON.fields_by_name['edge'].message_type = _BOUNDARYEDGE
_ROADBOUNDARY.fields_by_name['outer_polygon'].message_type = _BOUNDARYPOLYGON
_ROADBOUNDARY.fields_by_name['hole'].message_type = _BOUNDARYPOLYGON
_ROADROIBOUNDARY.fields_by_name['id'].message_type = modules_dot_map_dot_proto_dot_map__id__pb2._ID
_ROADROIBOUNDARY.fields_by_name['road_boundaries'].message_type = _ROADBOUNDARY
_ROADSECTION.fields_by_name['id'].message_type = modules_dot_map_dot_proto_dot_map__id__pb2._ID
_ROADSECTION.fields_by_name['lane_id'].message_type = modules_dot_map_dot_proto_dot_map__id__pb2._ID
_ROADSECTION.fields_by_name['boundary'].message_type = _ROADBOUNDARY
_ROAD.fields_by_name['id'].message_type = modules_dot_map_dot_proto_dot_map__id__pb2._ID
_ROAD.fields_by_name['section'].message_type = _ROADSECTION
_ROAD.fields_by_name['junction_id'].message_type = modules_dot_map_dot_proto_dot_map__id__pb2._ID
_ROAD.fields_by_name['type'].enum_type = _ROAD_TYPE
_ROAD_TYPE.containing_type = _ROAD
DESCRIPTOR.message_types_by_name['BoundaryEdge'] = _BOUNDARYEDGE
DESCRIPTOR.message_types_by_name['BoundaryPolygon'] = _BOUNDARYPOLYGON
DESCRIPTOR.message_types_by_name['RoadBoundary'] = _ROADBOUNDARY
DESCRIPTOR.message_types_by_name['RoadROIBoundary'] = _ROADROIBOUNDARY
DESCRIPTOR.message_types_by_name['RoadSection'] = _ROADSECTION
DESCRIPTOR.message_types_by_name['Road'] = _ROAD
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BoundaryEdge = _reflection.GeneratedProtocolMessageType('BoundaryEdge', (_message.Message,), dict(
  DESCRIPTOR = _BOUNDARYEDGE,
  __module__ = 'modules.map.proto.map_road_pb2'
  # @@protoc_insertion_point(class_scope:apollo.hdmap.BoundaryEdge)
  ))
_sym_db.RegisterMessage(BoundaryEdge)

BoundaryPolygon = _reflection.GeneratedProtocolMessageType('BoundaryPolygon', (_message.Message,), dict(
  DESCRIPTOR = _BOUNDARYPOLYGON,
  __module__ = 'modules.map.proto.map_road_pb2'
  # @@protoc_insertion_point(class_scope:apollo.hdmap.BoundaryPolygon)
  ))
_sym_db.RegisterMessage(BoundaryPolygon)

RoadBoundary = _reflection.GeneratedProtocolMessageType('RoadBoundary', (_message.Message,), dict(
  DESCRIPTOR = _ROADBOUNDARY,
  __module__ = 'modules.map.proto.map_road_pb2'
  # @@protoc_insertion_point(class_scope:apollo.hdmap.RoadBoundary)
  ))
_sym_db.RegisterMessage(RoadBoundary)

RoadROIBoundary = _reflection.GeneratedProtocolMessageType('RoadROIBoundary', (_message.Message,), dict(
  DESCRIPTOR = _ROADROIBOUNDARY,
  __module__ = 'modules.map.proto.map_road_pb2'
  # @@protoc_insertion_point(class_scope:apollo.hdmap.RoadROIBoundary)
  ))
_sym_db.RegisterMessage(RoadROIBoundary)

RoadSection = _reflection.GeneratedProtocolMessageType('RoadSection', (_message.Message,), dict(
  DESCRIPTOR = _ROADSECTION,
  __module__ = 'modules.map.proto.map_road_pb2'
  # @@protoc_insertion_point(class_scope:apollo.hdmap.RoadSection)
  ))
_sym_db.RegisterMessage(RoadSection)

Road = _reflection.GeneratedProtocolMessageType('Road', (_message.Message,), dict(
  DESCRIPTOR = _ROAD,
  __module__ = 'modules.map.proto.map_road_pb2'
  # @@protoc_insertion_point(class_scope:apollo.hdmap.Road)
  ))
_sym_db.RegisterMessage(Road)


# @@protoc_insertion_point(module_scope)
