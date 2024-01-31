from pydantic import BaseModel
from .stubs import product_pb2
from .stubs import basket_pb2 as b_pb2

import typing as t


class User(BaseModel):
    first_name: str
    email: str
    hash_password: str
    status: int
    active: bool


class UserModel(BaseModel):
    first_name: str
    email: str
    status: int
    active: bool


class UserRegisterRequest(BaseModel):
    first_name: str
    email: str
    password: str


class AuthRequest(BaseModel):
    email: str
    password: str


class ProductModel(BaseModel):
    title: str
    description: str
    price: float
    state: int

    def to_serialize(self) -> product_pb2.ProductObject:
        return product_pb2.ProductObject(
            title=self.title,
            description=self.description,
            price=self.price,
            state=product_pb2.ProductObject.State.Name(self.state)
        )


class BasketModel(BaseModel):
    user: str
    products: t.Iterable
    price: float


class ProductPosition(BaseModel):
    product: int
    coll: int


class AddProductBasket(BaseModel):
    user: str
    product_position: ProductPosition


class ShopModel(BaseModel):
    name: str
    description: str
