# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: modules/control/proto/pid_conf.proto

import sys

_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='modules/control/proto/pid_conf.proto',
  package='apollo.control',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n$modules/control/proto/pid_conf.proto\x12\x0e\x61pollo.control\"\x9e\x01\n\x07PidConf\x12\x19\n\x11integrator_enable\x18\x01 \x01(\x08\x12#\n\x1bintegrator_saturation_level\x18\x02 \x01(\x01\x12\n\n\x02kp\x18\x03 \x01(\x01\x12\n\n\x02ki\x18\x04 \x01(\x01\x12\n\n\x02kd\x18\x05 \x01(\x01\x12\x0e\n\x03kaw\x18\x06 \x01(\x01:\x01\x30\x12\x1f\n\x17output_saturation_level\x18\x07 \x01(\x01')
)




_PIDCONF = _descriptor.Descriptor(
  name='PidConf',
  full_name='apollo.control.PidConf',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='integrator_enable', full_name='apollo.control.PidConf.integrator_enable', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='integrator_saturation_level', full_name='apollo.control.PidConf.integrator_saturation_level', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='kp', full_name='apollo.control.PidConf.kp', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ki', full_name='apollo.control.PidConf.ki', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='kd', full_name='apollo.control.PidConf.kd', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='kaw', full_name='apollo.control.PidConf.kaw', index=5,
      number=6, type=1, cpp_type=5, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='output_saturation_level', full_name='apollo.control.PidConf.output_saturation_level', index=6,
      number=7, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=57,
  serialized_end=215,
)

DESCRIPTOR.message_types_by_name['PidConf'] = _PIDCONF
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PidConf = _reflection.GeneratedProtocolMessageType('PidConf', (_message.Message,), dict(
  DESCRIPTOR = _PIDCONF,
  __module__ = 'modules.control.proto.pid_conf_pb2'
  # @@protoc_insertion_point(class_scope:apollo.control.PidConf)
  ))
_sym_db.RegisterMessage(PidConf)


# @@protoc_insertion_point(module_scope)
