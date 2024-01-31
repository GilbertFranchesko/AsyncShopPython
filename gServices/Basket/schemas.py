from pydantic import BaseModel
import typing as t


class Product(BaseModel):
    id: int
    title: str
    price: float


class ProductPosition(BaseModel):
    product: Product
    coll: int


""" IBasket
Модель данных по типу Basket из basket_pb2.py
Сделанна для максимальной точности типизации.
"""


class IBasket(BaseModel):
    user: str
    products: t.List[ProductPosition]
    price: float
