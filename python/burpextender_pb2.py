# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: burpextender.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12\x62urpextender.proto\x1a\x19google/protobuf/any.proto\"@\n\x07Request\x12\x11\n\tfunc_name\x18\x01 \x01(\t\x12\"\n\x04\x61rgs\x18\x02 \x03(\x0b\x32\x14.google.protobuf.Any\"-\n\x08Response\x12!\n\x03res\x18\x01 \x01(\x0b\x32\x14.google.protobuf.Any22\n\x0f\x43\x61llFuncService\x12\x1f\n\x08\x43\x61llFunc\x12\x08.Request\x1a\t.Responseb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'burpextender_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _REQUEST._serialized_start=49
  _REQUEST._serialized_end=113
  _RESPONSE._serialized_start=115
  _RESPONSE._serialized_end=160
  _CALLFUNCSERVICE._serialized_start=162
  _CALLFUNCSERVICE._serialized_end=212
# @@protoc_insertion_point(module_scope)
