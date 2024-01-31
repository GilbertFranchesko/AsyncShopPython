# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: user.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nuser.proto\x12\x04user\"_\n\x04User\x12\n\n\x02id\x18\x01 \x01(\x04\x12\x12\n\nfirst_name\x18\x02 \x01(\t\x12\x11\n\tlast_name\x18\x03 \x01(\t\x12\r\n\x05\x65mail\x18\x04 \x01(\t\x12\x15\n\rhash_password\x18\x05 \x01(\t\"]\n\x13RegisterUserRequest\x12\x12\n\nfirst_name\x18\x01 \x01(\t\x12\x11\n\tlast_name\x18\x02 \x01(\t\x12\r\n\x05\x65mail\x18\x03 \x01(\t\x12\x10\n\x08password\x18\x04 \x01(\t\"8\n\x14RegisterUserResponse\x12 \n\x0c\x63reated_user\x18\x01 \x01(\x0b\x32\n.user.User\"\x11\n\x0fUserListRequest\"1\n\x10UserListResponse\x12\x1d\n\tuser_list\x18\x01 \x03(\x0b\x32\n.user.User\"7\n\x14UserAuthorizeRequest\x12\r\n\x05\x65mail\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\"\xab\x01\n\x15UserAuthorizeResponse\x12\x38\n\x06status\x18\x01 \x01(\x0e\x32(.user.UserAuthorizeResponse.AuthStatuses\x12\x1f\n\x0buser_schema\x18\x02 \x01(\x0b\x32\n.user.User\"7\n\x0c\x41uthStatuses\x12\n\n\x06\x46\x41ILED\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12\x0e\n\nNON_ACTIVE\x10\x02\"\x1b\n\tUserToken\x12\x0e\n\x06\x61\x63\x63\x65ss\x18\x01 \x01(\t2\xcd\x01\n\x0bUserService\x12\x41\n\x08Register\x12\x19.user.RegisterUserRequest\x1a\x1a.user.RegisterUserResponse\x12\x35\n\x04List\x12\x15.user.UserListRequest\x1a\x16.user.UserListResponse\x12\x44\n\tAuthorize\x12\x1a.user.UserAuthorizeRequest\x1a\x1b.user.UserAuthorizeResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'user_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_USER']._serialized_start=20
  _globals['_USER']._serialized_end=115
  _globals['_REGISTERUSERREQUEST']._serialized_start=117
  _globals['_REGISTERUSERREQUEST']._serialized_end=210
  _globals['_REGISTERUSERRESPONSE']._serialized_start=212
  _globals['_REGISTERUSERRESPONSE']._serialized_end=268
  _globals['_USERLISTREQUEST']._serialized_start=270
  _globals['_USERLISTREQUEST']._serialized_end=287
  _globals['_USERLISTRESPONSE']._serialized_start=289
  _globals['_USERLISTRESPONSE']._serialized_end=338
  _globals['_USERAUTHORIZEREQUEST']._serialized_start=340
  _globals['_USERAUTHORIZEREQUEST']._serialized_end=395
  _globals['_USERAUTHORIZERESPONSE']._serialized_start=398
  _globals['_USERAUTHORIZERESPONSE']._serialized_end=569
  _globals['_USERAUTHORIZERESPONSE_AUTHSTATUSES']._serialized_start=514
  _globals['_USERAUTHORIZERESPONSE_AUTHSTATUSES']._serialized_end=569
  _globals['_USERTOKEN']._serialized_start=571
  _globals['_USERTOKEN']._serialized_end=598
  _globals['_USERSERVICE']._serialized_start=601
  _globals['_USERSERVICE']._serialized_end=806
# @@protoc_insertion_point(module_scope)