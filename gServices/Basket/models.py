from piccolo.table import Table
from piccolo.columns import Varchar, JSON, Float
from piccolo_conf import DB

from stubs import basket_pb2
import json


class BasketTable(Table, db=DB):
    user = Varchar()
    productsPosition = JSON()
    price = Float()

    @staticmethod
    def serialize(obj):
        dumpped_products_position = list()
        for product_position in json.loads(obj["productsPosition"]):
            product_position["product"]["id"] = int(product_position["product"]["id"])
            dumpped_products_position.append(basket_pb2.ProductPosition(**product_position))
        obj["productsPosition"] = dumpped_products_position
        return obj
