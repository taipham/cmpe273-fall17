# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: datastore.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='datastore.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\x0f\x64\x61tastore.proto\"\x0e\n\x0c\x45mptyRequest\"\x17\n\x07Request\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\t\"\x18\n\x08Response\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\t\")\n\x0bResponseRep\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\"\x1a\n\nRequestInt\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\x05\x32p\n\tDatastore\x12\x1c\n\x03put\x12\x08.Request\x1a\t.Response\"\x00\x12\x1c\n\x03get\x12\x08.Request\x1a\t.Response\"\x00\x12\'\n\treplicate\x12\x0b.RequestInt\x1a\t.Response\"\x00\x30\x01\x62\x06proto3')
)




_EMPTYREQUEST = _descriptor.Descriptor(
  name='EmptyRequest',
  full_name='EmptyRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=19,
  serialized_end=33,
)


_REQUEST = _descriptor.Descriptor(
  name='Request',
  full_name='Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='Request.data', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=35,
  serialized_end=58,
)


_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='Response.data', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=60,
  serialized_end=84,
)


_RESPONSEREP = _descriptor.Descriptor(
  name='ResponseRep',
  full_name='ResponseRep',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='ResponseRep.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='ResponseRep.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=86,
  serialized_end=127,
)


_REQUESTINT = _descriptor.Descriptor(
  name='RequestInt',
  full_name='RequestInt',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='RequestInt.data', index=0,
      number=1, type=5, cpp_type=1, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=129,
  serialized_end=155,
)

DESCRIPTOR.message_types_by_name['EmptyRequest'] = _EMPTYREQUEST
DESCRIPTOR.message_types_by_name['Request'] = _REQUEST
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE
DESCRIPTOR.message_types_by_name['ResponseRep'] = _RESPONSEREP
DESCRIPTOR.message_types_by_name['RequestInt'] = _REQUESTINT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

EmptyRequest = _reflection.GeneratedProtocolMessageType('EmptyRequest', (_message.Message,), dict(
  DESCRIPTOR = _EMPTYREQUEST,
  __module__ = 'datastore_pb2'
  # @@protoc_insertion_point(class_scope:EmptyRequest)
  ))
_sym_db.RegisterMessage(EmptyRequest)

Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), dict(
  DESCRIPTOR = _REQUEST,
  __module__ = 'datastore_pb2'
  # @@protoc_insertion_point(class_scope:Request)
  ))
_sym_db.RegisterMessage(Request)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), dict(
  DESCRIPTOR = _RESPONSE,
  __module__ = 'datastore_pb2'
  # @@protoc_insertion_point(class_scope:Response)
  ))
_sym_db.RegisterMessage(Response)

ResponseRep = _reflection.GeneratedProtocolMessageType('ResponseRep', (_message.Message,), dict(
  DESCRIPTOR = _RESPONSEREP,
  __module__ = 'datastore_pb2'
  # @@protoc_insertion_point(class_scope:ResponseRep)
  ))
_sym_db.RegisterMessage(ResponseRep)

RequestInt = _reflection.GeneratedProtocolMessageType('RequestInt', (_message.Message,), dict(
  DESCRIPTOR = _REQUESTINT,
  __module__ = 'datastore_pb2'
  # @@protoc_insertion_point(class_scope:RequestInt)
  ))
_sym_db.RegisterMessage(RequestInt)


try:
  # THESE ELEMENTS WILL BE DEPRECATED.
  # Please use the generated *_pb2_grpc.py files instead.
  import grpc
  from grpc.beta import implementations as beta_implementations
  from grpc.beta import interfaces as beta_interfaces
  from grpc.framework.common import cardinality
  from grpc.framework.interfaces.face import utilities as face_utilities


  class DatastoreStub(object):
    # missing associated documentation comment in .proto file
    pass

    def __init__(self, channel):
      """Constructor.

      Args:
        channel: A grpc.Channel.
      """
      self.put = channel.unary_unary(
          '/Datastore/put',
          request_serializer=Request.SerializeToString,
          response_deserializer=Response.FromString,
          )
      self.get = channel.unary_unary(
          '/Datastore/get',
          request_serializer=Request.SerializeToString,
          response_deserializer=Response.FromString,
          )
      self.replicate = channel.unary_stream(
          '/Datastore/replicate',
          request_serializer=RequestInt.SerializeToString,
          response_deserializer=Response.FromString,
          )


  class DatastoreServicer(object):
    # missing associated documentation comment in .proto file
    pass

    def put(self, request, context):
      # missing associated documentation comment in .proto file
      pass
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')

    def get(self, request, context):
      # missing associated documentation comment in .proto file
      pass
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')

    def replicate(self, request, context):
      # missing associated documentation comment in .proto file
      pass
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')


  def add_DatastoreServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'put': grpc.unary_unary_rpc_method_handler(
            servicer.put,
            request_deserializer=Request.FromString,
            response_serializer=Response.SerializeToString,
        ),
        'get': grpc.unary_unary_rpc_method_handler(
            servicer.get,
            request_deserializer=Request.FromString,
            response_serializer=Response.SerializeToString,
        ),
        'replicate': grpc.unary_stream_rpc_method_handler(
            servicer.replicate,
            request_deserializer=RequestInt.FromString,
            response_serializer=Response.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'Datastore', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


  class BetaDatastoreServicer(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    # missing associated documentation comment in .proto file
    pass
    def put(self, request, context):
      # missing associated documentation comment in .proto file
      pass
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
    def get(self, request, context):
      # missing associated documentation comment in .proto file
      pass
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
    def replicate(self, request, context):
      # missing associated documentation comment in .proto file
      pass
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)


  class BetaDatastoreStub(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    # missing associated documentation comment in .proto file
    pass
    def put(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      # missing associated documentation comment in .proto file
      pass
      raise NotImplementedError()
    put.future = None
    def get(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      # missing associated documentation comment in .proto file
      pass
      raise NotImplementedError()
    get.future = None
    def replicate(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      # missing associated documentation comment in .proto file
      pass
      raise NotImplementedError()


  def beta_create_Datastore_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_deserializers = {
      ('Datastore', 'get'): Request.FromString,
      ('Datastore', 'put'): Request.FromString,
      ('Datastore', 'replicate'): RequestInt.FromString,
    }
    response_serializers = {
      ('Datastore', 'get'): Response.SerializeToString,
      ('Datastore', 'put'): Response.SerializeToString,
      ('Datastore', 'replicate'): Response.SerializeToString,
    }
    method_implementations = {
      ('Datastore', 'get'): face_utilities.unary_unary_inline(servicer.get),
      ('Datastore', 'put'): face_utilities.unary_unary_inline(servicer.put),
      ('Datastore', 'replicate'): face_utilities.unary_stream_inline(servicer.replicate),
    }
    server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
    return beta_implementations.server(method_implementations, options=server_options)


  def beta_create_Datastore_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_serializers = {
      ('Datastore', 'get'): Request.SerializeToString,
      ('Datastore', 'put'): Request.SerializeToString,
      ('Datastore', 'replicate'): RequestInt.SerializeToString,
    }
    response_deserializers = {
      ('Datastore', 'get'): Response.FromString,
      ('Datastore', 'put'): Response.FromString,
      ('Datastore', 'replicate'): Response.FromString,
    }
    cardinalities = {
      'get': cardinality.Cardinality.UNARY_UNARY,
      'put': cardinality.Cardinality.UNARY_UNARY,
      'replicate': cardinality.Cardinality.UNARY_STREAM,
    }
    stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
    return beta_implementations.dynamic_stub(channel, 'Datastore', cardinalities, options=stub_options)
except ImportError:
  pass
# @@protoc_insertion_point(module_scope)
