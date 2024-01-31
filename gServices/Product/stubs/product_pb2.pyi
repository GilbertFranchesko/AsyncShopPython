from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ProductObject(_message.Message):
    __slots__ = ["id", "title", "description", "price", "state"]
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
        IN_ROUTE: _ClassVar[ProductObject.State]
        ACTIVE: _ClassVar[ProductObject.State]
        DISABLE: _ClassVar[ProductObject.State]
    IN_ROUTE: ProductObject.State
    ACTIVE: ProductObject.State
    DISABLE: ProductObject.State
    ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    id: int
    title: str
    description: str
    price: float
    state: ProductObject.State
    def __init__(self, id: _Optional[int] = ..., title: _Optional[str] = ..., description: _Optional[str] = ..., price: _Optional[float] = ..., state: _Optional[_Union[ProductObject.State, str]] = ...) -> None: ...

class ProductListRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ProductListResponse(_message.Message):
    __slots__ = ["products"]
    PRODUCTS_FIELD_NUMBER: _ClassVar[int]
    products: _containers.RepeatedCompositeFieldContainer[ProductObject]
    def __init__(self, products: _Optional[_Iterable[_Union[ProductObject, _Mapping]]] = ...) -> None: ...

class DeleteProductRequest(_message.Message):
    __slots__ = ["product_id"]
    PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    product_id: int
    def __init__(self, product_id: _Optional[int] = ...) -> None: ...

class DeleteProductResponse(_message.Message):
    __slots__ = ["success"]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool
    def __init__(self, success: bool = ...) -> None: ...

class ReadProductRequest(_message.Message):
    __slots__ = ["product_id"]
    PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    product_id: int
    def __init__(self, product_id: _Optional[int] = ...) -> None: ...

class ReadProductResponse(_message.Message):
    __slots__ = ["product"]
    PRODUCT_FIELD_NUMBER: _ClassVar[int]
    product: ProductObject
    def __init__(self, product: _Optional[_Union[ProductObject, _Mapping]] = ...) -> None: ...

class AddProductResponse(_message.Message):
    __slots__ = ["product"]
    PRODUCT_FIELD_NUMBER: _ClassVar[int]
    product: ProductObject
    def __init__(self, product: _Optional[_Union[ProductObject, _Mapping]] = ...) -> None: ...

class EditProductRequest(_message.Message):
    __slots__ = ["product"]
    PRODUCT_FIELD_NUMBER: _ClassVar[int]
    product: ProductObject
    def __init__(self, product: _Optional[_Union[ProductObject, _Mapping]] = ...) -> None: ...

class EditProductResponse(_message.Message):
    __slots__ = ["product"]
    PRODUCT_FIELD_NUMBER: _ClassVar[int]
    product: ProductObject
    def __init__(self, product: _Optional[_Union[ProductObject, _Mapping]] = ...) -> None: ...
