# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: src/kRPC/Schema/KRPC.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='src/kRPC/Schema/KRPC.proto',
  package='krpc',
  serialized_pb='\n\x1asrc/kRPC/Schema/KRPC.proto\x12\x04krpc\"P\n\x07Request\x12\x0f\n\x07service\x18\x01 \x02(\t\x12\x11\n\tprocedure\x18\x02 \x02(\t\x12!\n\targuments\x18\x03 \x03(\x0b\x32\x0e.krpc.Argument\"+\n\x08\x41rgument\x12\x10\n\x08position\x18\x01 \x02(\r\x12\r\n\x05value\x18\x02 \x02(\x0c\"=\n\x08Response\x12\x0c\n\x04time\x18\x01 \x02(\x01\x12\r\n\x05\x65rror\x18\x02 \x01(\t\x12\x14\n\x0creturn_value\x18\x03 \x01(\x0c\"8\n\rStreamMessage\x12\'\n\tresponses\x18\x01 \x03(\x0b\x32\x14.krpc.StreamResponse\">\n\x0eStreamResponse\x12\n\n\x02id\x18\x01 \x02(\r\x12 \n\x08response\x18\x02 \x02(\x0b\x32\x0e.krpc.Response\"+\n\x08Services\x12\x1f\n\x08services\x18\x01 \x03(\x0b\x32\r.krpc.Service\"\x83\x01\n\x07Service\x12\x0c\n\x04name\x18\x01 \x02(\t\x12#\n\nprocedures\x18\x02 \x03(\x0b\x32\x0f.krpc.Procedure\x12\x1c\n\x07\x63lasses\x18\x03 \x03(\x0b\x32\x0b.krpc.Class\x12\'\n\x0c\x65numerations\x18\x04 \x03(\x0b\x32\x11.krpc.Enumeration\"g\n\tProcedure\x12\x0c\n\x04name\x18\x01 \x02(\t\x12#\n\nparameters\x18\x02 \x03(\x0b\x32\x0f.krpc.Parameter\x12\x13\n\x0breturn_type\x18\x03 \x01(\t\x12\x12\n\nattributes\x18\x04 \x03(\t\"A\n\tParameter\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\x0c\n\x04type\x18\x02 \x02(\t\x12\x18\n\x10\x64\x65\x66\x61ult_argument\x18\x03 \x01(\x0c\"\x15\n\x05\x43lass\x12\x0c\n\x04name\x18\x01 \x02(\t\"C\n\x0b\x45numeration\x12\x0c\n\x04name\x18\x01 \x02(\t\x12&\n\x06values\x18\x02 \x03(\x0b\x32\x16.krpc.EnumerationValue\"/\n\x10\x45numerationValue\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\r\n\x05value\x18\x02 \x02(\x05\"\x15\n\x04List\x12\r\n\x05items\x18\x01 \x03(\x0c\"4\n\nDictionary\x12&\n\x07\x65ntries\x18\x01 \x03(\x0b\x32\x15.krpc.DictionaryEntry\"-\n\x0f\x44ictionaryEntry\x12\x0b\n\x03key\x18\x01 \x02(\x0c\x12\r\n\x05value\x18\x02 \x02(\x0c\"\x14\n\x03Set\x12\r\n\x05items\x18\x01 \x03(\x0c\"\x16\n\x05Tuple\x12\r\n\x05items\x18\x01 \x03(\x0c\"\x19\n\x06Status\x12\x0f\n\x07version\x18\x01 \x02(\t')




_REQUEST = _descriptor.Descriptor(
  name='Request',
  full_name='krpc.Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='service', full_name='krpc.Request.service', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='procedure', full_name='krpc.Request.procedure', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='arguments', full_name='krpc.Request.arguments', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=36,
  serialized_end=116,
)


_ARGUMENT = _descriptor.Descriptor(
  name='Argument',
  full_name='krpc.Argument',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='position', full_name='krpc.Argument.position', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='krpc.Argument.value', index=1,
      number=2, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=118,
  serialized_end=161,
)


_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='krpc.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='time', full_name='krpc.Response.time', index=0,
      number=1, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='error', full_name='krpc.Response.error', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='return_value', full_name='krpc.Response.return_value', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=163,
  serialized_end=224,
)


_STREAMMESSAGE = _descriptor.Descriptor(
  name='StreamMessage',
  full_name='krpc.StreamMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='responses', full_name='krpc.StreamMessage.responses', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=226,
  serialized_end=282,
)


_STREAMRESPONSE = _descriptor.Descriptor(
  name='StreamResponse',
  full_name='krpc.StreamResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='krpc.StreamResponse.id', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='response', full_name='krpc.StreamResponse.response', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=284,
  serialized_end=346,
)


_SERVICES = _descriptor.Descriptor(
  name='Services',
  full_name='krpc.Services',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='services', full_name='krpc.Services.services', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=348,
  serialized_end=391,
)


_SERVICE = _descriptor.Descriptor(
  name='Service',
  full_name='krpc.Service',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='krpc.Service.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='procedures', full_name='krpc.Service.procedures', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='classes', full_name='krpc.Service.classes', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='enumerations', full_name='krpc.Service.enumerations', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=394,
  serialized_end=525,
)


_PROCEDURE = _descriptor.Descriptor(
  name='Procedure',
  full_name='krpc.Procedure',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='krpc.Procedure.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='parameters', full_name='krpc.Procedure.parameters', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='return_type', full_name='krpc.Procedure.return_type', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='attributes', full_name='krpc.Procedure.attributes', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=527,
  serialized_end=630,
)


_PARAMETER = _descriptor.Descriptor(
  name='Parameter',
  full_name='krpc.Parameter',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='krpc.Parameter.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='krpc.Parameter.type', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='default_argument', full_name='krpc.Parameter.default_argument', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=632,
  serialized_end=697,
)


_CLASS = _descriptor.Descriptor(
  name='Class',
  full_name='krpc.Class',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='krpc.Class.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=699,
  serialized_end=720,
)


_ENUMERATION = _descriptor.Descriptor(
  name='Enumeration',
  full_name='krpc.Enumeration',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='krpc.Enumeration.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='values', full_name='krpc.Enumeration.values', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=722,
  serialized_end=789,
)


_ENUMERATIONVALUE = _descriptor.Descriptor(
  name='EnumerationValue',
  full_name='krpc.EnumerationValue',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='krpc.EnumerationValue.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='krpc.EnumerationValue.value', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=791,
  serialized_end=838,
)


_LIST = _descriptor.Descriptor(
  name='List',
  full_name='krpc.List',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='items', full_name='krpc.List.items', index=0,
      number=1, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=840,
  serialized_end=861,
)


_DICTIONARY = _descriptor.Descriptor(
  name='Dictionary',
  full_name='krpc.Dictionary',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='entries', full_name='krpc.Dictionary.entries', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=863,
  serialized_end=915,
)


_DICTIONARYENTRY = _descriptor.Descriptor(
  name='DictionaryEntry',
  full_name='krpc.DictionaryEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='krpc.DictionaryEntry.key', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='krpc.DictionaryEntry.value', index=1,
      number=2, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=917,
  serialized_end=962,
)


_SET = _descriptor.Descriptor(
  name='Set',
  full_name='krpc.Set',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='items', full_name='krpc.Set.items', index=0,
      number=1, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=964,
  serialized_end=984,
)


_TUPLE = _descriptor.Descriptor(
  name='Tuple',
  full_name='krpc.Tuple',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='items', full_name='krpc.Tuple.items', index=0,
      number=1, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=986,
  serialized_end=1008,
)


_STATUS = _descriptor.Descriptor(
  name='Status',
  full_name='krpc.Status',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='version', full_name='krpc.Status.version', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1010,
  serialized_end=1035,
)

_REQUEST.fields_by_name['arguments'].message_type = _ARGUMENT
_STREAMMESSAGE.fields_by_name['responses'].message_type = _STREAMRESPONSE
_STREAMRESPONSE.fields_by_name['response'].message_type = _RESPONSE
_SERVICES.fields_by_name['services'].message_type = _SERVICE
_SERVICE.fields_by_name['procedures'].message_type = _PROCEDURE
_SERVICE.fields_by_name['classes'].message_type = _CLASS
_SERVICE.fields_by_name['enumerations'].message_type = _ENUMERATION
_PROCEDURE.fields_by_name['parameters'].message_type = _PARAMETER
_ENUMERATION.fields_by_name['values'].message_type = _ENUMERATIONVALUE
_DICTIONARY.fields_by_name['entries'].message_type = _DICTIONARYENTRY
DESCRIPTOR.message_types_by_name['Request'] = _REQUEST
DESCRIPTOR.message_types_by_name['Argument'] = _ARGUMENT
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE
DESCRIPTOR.message_types_by_name['StreamMessage'] = _STREAMMESSAGE
DESCRIPTOR.message_types_by_name['StreamResponse'] = _STREAMRESPONSE
DESCRIPTOR.message_types_by_name['Services'] = _SERVICES
DESCRIPTOR.message_types_by_name['Service'] = _SERVICE
DESCRIPTOR.message_types_by_name['Procedure'] = _PROCEDURE
DESCRIPTOR.message_types_by_name['Parameter'] = _PARAMETER
DESCRIPTOR.message_types_by_name['Class'] = _CLASS
DESCRIPTOR.message_types_by_name['Enumeration'] = _ENUMERATION
DESCRIPTOR.message_types_by_name['EnumerationValue'] = _ENUMERATIONVALUE
DESCRIPTOR.message_types_by_name['List'] = _LIST
DESCRIPTOR.message_types_by_name['Dictionary'] = _DICTIONARY
DESCRIPTOR.message_types_by_name['DictionaryEntry'] = _DICTIONARYENTRY
DESCRIPTOR.message_types_by_name['Set'] = _SET
DESCRIPTOR.message_types_by_name['Tuple'] = _TUPLE
DESCRIPTOR.message_types_by_name['Status'] = _STATUS

class Request(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _REQUEST

  # @@protoc_insertion_point(class_scope:krpc.Request)

class Argument(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ARGUMENT

  # @@protoc_insertion_point(class_scope:krpc.Argument)

class Response(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _RESPONSE

  # @@protoc_insertion_point(class_scope:krpc.Response)

class StreamMessage(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _STREAMMESSAGE

  # @@protoc_insertion_point(class_scope:krpc.StreamMessage)

class StreamResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _STREAMRESPONSE

  # @@protoc_insertion_point(class_scope:krpc.StreamResponse)

class Services(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _SERVICES

  # @@protoc_insertion_point(class_scope:krpc.Services)

class Service(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _SERVICE

  # @@protoc_insertion_point(class_scope:krpc.Service)

class Procedure(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PROCEDURE

  # @@protoc_insertion_point(class_scope:krpc.Procedure)

class Parameter(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PARAMETER

  # @@protoc_insertion_point(class_scope:krpc.Parameter)

class Class(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CLASS

  # @@protoc_insertion_point(class_scope:krpc.Class)

class Enumeration(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ENUMERATION

  # @@protoc_insertion_point(class_scope:krpc.Enumeration)

class EnumerationValue(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ENUMERATIONVALUE

  # @@protoc_insertion_point(class_scope:krpc.EnumerationValue)

class List(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _LIST

  # @@protoc_insertion_point(class_scope:krpc.List)

class Dictionary(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _DICTIONARY

  # @@protoc_insertion_point(class_scope:krpc.Dictionary)

class DictionaryEntry(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _DICTIONARYENTRY

  # @@protoc_insertion_point(class_scope:krpc.DictionaryEntry)

class Set(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _SET

  # @@protoc_insertion_point(class_scope:krpc.Set)

class Tuple(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _TUPLE

  # @@protoc_insertion_point(class_scope:krpc.Tuple)

class Status(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _STATUS

  # @@protoc_insertion_point(class_scope:krpc.Status)


# @@protoc_insertion_point(module_scope)