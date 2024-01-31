from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class User(_message.Message):
    __slots__ = ["id", "first_name", "last_name", "email", "hash_password"]
    ID_FIELD_NUMBER: _ClassVar[int]
    FIRST_NAME_FIELD_NUMBER: _ClassVar[int]
    LAST_NAME_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    HASH_PASSWORD_FIELD_NUMBER: _ClassVar[int]
    id: int
    first_name: str
    last_name: str
    email: str
    hash_password: str
    def __init__(self, id: _Optional[int] = ..., first_name: _Optional[str] = ..., last_name: _Optional[str] = ..., email: _Optional[str] = ..., hash_password: _Optional[str] = ...) -> None: ...

class RegisterUserRequest(_message.Message):
    __slots__ = ["first_name", "last_name", "email", "password"]
    FIRST_NAME_FIELD_NUMBER: _ClassVar[int]
    LAST_NAME_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    first_name: str
    last_name: str
    email: str
    password: str
    def __init__(self, first_name: _Optional[str] = ..., last_name: _Optional[str] = ..., email: _Optional[str] = ..., password: _Optional[str] = ...) -> None: ...

class RegisterUserResponse(_message.Message):
    __slots__ = ["created_user"]
    CREATED_USER_FIELD_NUMBER: _ClassVar[int]
    created_user: User
    def __init__(self, created_user: _Optional[_Union[User, _Mapping]] = ...) -> None: ...

class UserListRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class UserListResponse(_message.Message):
    __slots__ = ["user_list"]
    USER_LIST_FIELD_NUMBER: _ClassVar[int]
    user_list: _containers.RepeatedCompositeFieldContainer[User]
    def __init__(self, user_list: _Optional[_Iterable[_Union[User, _Mapping]]] = ...) -> None: ...

class UserAuthorizeRequest(_message.Message):
    __slots__ = ["email", "password"]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    email: str
    password: str
    def __init__(self, email: _Optional[str] = ..., password: _Optional[str] = ...) -> None: ...

class UserAuthorizeResponse(_message.Message):
    __slots__ = ["status", "user_schema"]
    class AuthStatuses(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
        FAILED: _ClassVar[UserAuthorizeResponse.AuthStatuses]
        SUCCESS: _ClassVar[UserAuthorizeResponse.AuthStatuses]
        NON_ACTIVE: _ClassVar[UserAuthorizeResponse.AuthStatuses]
    FAILED: UserAuthorizeResponse.AuthStatuses
    SUCCESS: UserAuthorizeResponse.AuthStatuses
    NON_ACTIVE: UserAuthorizeResponse.AuthStatuses
    STATUS_FIELD_NUMBER: _ClassVar[int]
    USER_SCHEMA_FIELD_NUMBER: _ClassVar[int]
    status: UserAuthorizeResponse.AuthStatuses
    user_schema: User
    def __init__(self, status: _Optional[_Union[UserAuthorizeResponse.AuthStatuses, str]] = ..., user_schema: _Optional[_Union[User, _Mapping]] = ...) -> None: ...

class UserToken(_message.Message):
    __slots__ = ["access"]
    ACCESS_FIELD_NUMBER: _ClassVar[int]
    access: str
    def __init__(self, access: _Optional[str] = ...) -> None: ...
