# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: modules/map/relative_map/proto/navigator_config.proto

import sys

_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='modules/map/relative_map/proto/navigator_config.proto',
  package='apollo.relative_map',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n5modules/map/relative_map/proto/navigator_config.proto\x12\x13\x61pollo.relative_map\"\x83\x02\n\x0bSampleParam\x12#\n\x18straight_sample_interval\x18\x01 \x01(\x01:\x01\x33\x12&\n\x1bsmall_kappa_sample_interval\x18\x02 \x01(\x01:\x01\x31\x12)\n\x1cmiddle_kappa_sample_interval\x18\x03 \x01(\x01:\x03\x30.4\x12(\n\x1blarge_kappa_sample_interval\x18\x04 \x01(\x01:\x03\x30.1\x12\x1a\n\x0bsmall_kappa\x18\x05 \x01(\x01:\x05\x30.002\x12\x1b\n\x0cmiddle_kappa\x18\x06 \x01(\x01:\x05\x30.008\x12\x19\n\x0blarge_kappa\x18\x07 \x01(\x01:\x04\x30.02\"t\n\x0fNavigatorConfig\x12)\n\x1b\x65nable_navigator_downsample\x18\x01 \x01(\x08:\x04true\x12\x36\n\x0csample_param\x18\x02 \x01(\x0b\x32 .apollo.relative_map.SampleParam')
)




_SAMPLEPARAM = _descriptor.Descriptor(
  name='SampleParam',
  full_name='apollo.relative_map.SampleParam',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='straight_sample_interval', full_name='apollo.relative_map.SampleParam.straight_sample_interval', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=True, default_value=float(3),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='small_kappa_sample_interval', full_name='apollo.relative_map.SampleParam.small_kappa_sample_interval', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=True, default_value=float(1),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='middle_kappa_sample_interval', full_name='apollo.relative_map.SampleParam.middle_kappa_sample_interval', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=True, default_value=float(0.4),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='large_kappa_sample_interval', full_name='apollo.relative_map.SampleParam.large_kappa_sample_interval', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=True, default_value=float(0.1),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='small_kappa', full_name='apollo.relative_map.SampleParam.small_kappa', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=True, default_value=float(0.002),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='middle_kappa', full_name='apollo.relative_map.SampleParam.middle_kappa', index=5,
      number=6, type=1, cpp_type=5, label=1,
      has_default_value=True, default_value=float(0.008),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='large_kappa', full_name='apollo.relative_map.SampleParam.large_kappa', index=6,
      number=7, type=1, cpp_type=5, label=1,
      has_default_value=True, default_value=float(0.02),
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
  serialized_start=79,
  serialized_end=338,
)


_NAVIGATORCONFIG = _descriptor.Descriptor(
  name='NavigatorConfig',
  full_name='apollo.relative_map.NavigatorConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='enable_navigator_downsample', full_name='apollo.relative_map.NavigatorConfig.enable_navigator_downsample', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=True,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sample_param', full_name='apollo.relative_map.NavigatorConfig.sample_param', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_start=340,
  serialized_end=456,
)

_NAVIGATORCONFIG.fields_by_name['sample_param'].message_type = _SAMPLEPARAM
DESCRIPTOR.message_types_by_name['SampleParam'] = _SAMPLEPARAM
DESCRIPTOR.message_types_by_name['NavigatorConfig'] = _NAVIGATORCONFIG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SampleParam = _reflection.GeneratedProtocolMessageType('SampleParam', (_message.Message,), dict(
  DESCRIPTOR = _SAMPLEPARAM,
  __module__ = 'modules.map.relative_map.proto.navigator_config_pb2'
  # @@protoc_insertion_point(class_scope:apollo.relative_map.SampleParam)
  ))
_sym_db.RegisterMessage(SampleParam)

NavigatorConfig = _reflection.GeneratedProtocolMessageType('NavigatorConfig', (_message.Message,), dict(
  DESCRIPTOR = _NAVIGATORCONFIG,
  __module__ = 'modules.map.relative_map.proto.navigator_config_pb2'
  # @@protoc_insertion_point(class_scope:apollo.relative_map.NavigatorConfig)
  ))
_sym_db.RegisterMessage(NavigatorConfig)


# @@protoc_insertion_point(module_scope)
