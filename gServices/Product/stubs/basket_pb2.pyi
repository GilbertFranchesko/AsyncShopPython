import product_pb2 as _product_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ProductPosition(_message.Message):
    __slots__ = ["product", "coll"]
    PRODUCT_FIELD_NUMBER: _ClassVar[int]
    COLL_FIELD_NUMBER: _ClassVar[int]
    product: _product_pb2.ProductObject
    coll: int
    def __init__(self, product: _Optional[_Union[_product_pb2.ProductObject, _Mapping]] = ..., coll: _Optional[int] = ...) -> None: ...

class Basket(_message.Message):
    __slots__ = ["id", "user", "productsPosition", "price"]
    ID_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    PRODUCTSPOSITION_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    id: int
    user: str
    productsPosition: _containers.RepeatedCompositeFieldContainer[ProductPosition]
    price: float
    def __init__(self, id: _Optional[int] = ..., user: _Optional[str] = ..., productsPosition: _Optional[_Iterable[_Union[ProductPosition, _Mapping]]] = ..., price: _Optional[float] = ...) -> None: ...

class CreateBasketRequest(_message.Message):
    __slots__ = ["user", "productPosition"]
    USER_FIELD_NUMBER: _ClassVar[int]
    PRODUCTPOSITION_FIELD_NUMBER: _ClassVar[int]
    user: str
    productPosition: ProductPosition
    def __init__(self, user: _Optional[str] = ..., productPosition: _Optional[_Union[ProductPosition, _Mapping]] = ...) -> None: ...

class CreateBasketResponse(_message.Message):
    __slots__ = ["basket"]
    BASKET_FIELD_NUMBER: _ClassVar[int]
    basket: Basket
    def __init__(self, basket: _Optional[_Union[Basket, _Mapping]] = ...) -> None: ...

class ListBasketRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ListBasketResponse(_message.Message):
    __slots__ = ["baskets"]
    BASKETS_FIELD_NUMBER: _ClassVar[int]
    baskets: _containers.RepeatedCompositeFieldContainer[Basket]
    def __init__(self, baskets: _Optional[_Iterable[_Union[Basket, _Mapping]]] = ...) -> None: ...

class AddProductRequest(_message.Message):
    __slots__ = ["user", "productPosition"]
    USER_FIELD_NUMBER: _ClassVar[int]
    PRODUCTPOSITION_FIELD_NUMBER: _ClassVar[int]
    user: str
    productPosition: ProductPosition
    def __init__(self, user: _Optional[str] = ..., productPosition: _Optional[_Union[ProductPosition, _Mapping]] = ...) -> None: ...

class AddProductResponse(_message.Message):
    __slots__ = ["basket"]
    BASKET_FIELD_NUMBER: _ClassVar[int]
    basket: Basket
    def __init__(self, basket: _Optional[_Union[Basket, _Mapping]] = ...) -> None: ...

class RemoveProductRequest(_message.Message):
    __slots__ = ["product"]
    PRODUCT_FIELD_NUMBER: _ClassVar[int]
    product: _product_pb2.ProductObject
    def __init__(self, product: _Optional[_Union[_product_pb2.ProductObject, _Mapping]] = ...) -> None: ...

class RemoveProductResponse(_message.Message):
    __slots__ = ["basket"]
    BASKET_FIELD_NUMBER: _ClassVar[int]
    basket: Basket
    def __init__(self, basket: _Optional[_Union[Basket, _Mapping]] = ...) -> None: ...
