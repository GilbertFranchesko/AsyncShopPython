import typing as t
import json
from models import BasketTable
from product_client import product_stub
from stubs import product_pb2 as p_pb2
from piccolo.table import create_db_tables
from google.protobuf.json_format import MessageToDict

from schemas import IBasket, ProductPosition, Product
from decorators import mixed_results


async def db_unit():
    await create_db_tables(BasketTable, if_not_exists=True)

"""
    Функция инициализации общей стоимости корзины
    Args:
        - products_position: позиции в корзине (ид товара и кол-во)
    Return:
        - float: общая сумма
"""


def init_price_for_basket(products_position: t.List[ProductPosition]) -> float:
    return sum([product_position.product.price * product_position.coll for product_position in products_position])


""" Фун-ция проверки продукта
    Args:
        - product_id
        - coll - количество этого продукта #TODO: потом сделать проверку
            есть ли заданное кол-во у продавца. 
    Returns:
        - tuple:
            - обьект ReadProductResponse()
            - обьект Product (который задан в аргументе декоратора)
"""


@mixed_results(Product, first_key="product")
async def check_product(product_id: int, coll: int = 0) -> t.Tuple:
    product_client = await product_stub()
    product = await product_client.Read(p_pb2.ReadProductRequest(product_id=product_id))
    return product


""" Функция списка всех корзин
    Описания думаю не нужно.
    #TODO: Вскорем сделать какой-то CRUD декоратор или что то того
"""


async def list_of_basket(limit: int = 20):
    baskets = await BasketTable.select().limit(limit)
    list_of_baskets = []
    for basket in baskets:
        list_of_baskets.append(BasketTable.serialize(basket))

    return list_of_baskets

""" Инициализация корзины
    Args:
        - user: str: имя юзера
        - product_position: ОДНА позиция товара.
    
    За одной позицией мы и инициализируем корзину, добавить сразу две
    невозможно, ибо при создании первой корзина уже будет создана.
    Returns:
        - basket: IBasket - созданная корзина в обьекте IBasket
"""

async def init_basket(user: str, product_position: ProductPosition) -> IBasket:
    # Check the product and get the product object
    product, product_object = await check_product(product_position.product.id, product_position.coll)
    
    # Initialize the ProductPosition object with data from the request
    product_pos = ProductPosition(product=product_object, coll=product_position.coll)

    # Return the previously created object wrapped in a list
    price_of_product = init_price_for_basket([product_pos])

    # Convert positions to JSON string for adding to the database
    product_dict = MessageToDict(product)
    product_dict["coll"] = product_position.coll

    # Check if the user already has a basket
    user_basket = await select_basket_by_user(user)
    if user_basket is not None:
        products_position: list = json.loads(user_basket["productsPosition"])
        products_position.append(product_dict)

        # Convert updated positions to ProductPosition objects
        serial_positions = [ProductPosition(**dict_product_pos) for dict_product_pos in products_position]
        same_price = init_price_for_basket(serial_positions)

        products_to_json = json.dumps(products_position)
        await BasketTable.update(
            productsPosition=products_to_json,
            price=same_price
        ).where(BasketTable.id == user_basket["id"])

        updated_table = await BasketTable.select().where(BasketTable.id == user_basket["id"])

        # Serialize and return the updated basket
        return BasketTable.serialize(updated_table[0])

    products_to_json = json.dumps([product_dict])

    # Insert a new basket if the user doesn't have one yet
    basket = await BasketTable.insert(
        BasketTable(
            user=user,
            productsPosition=products_to_json,
            price=price_of_product
        ))

    return basket[0]


async def select_basket_by_user(user: str) -> t.Optional[dict]:
    basket = await BasketTable.select().where(BasketTable.user == user)
    print("Select basket: ", user ," ",basket)
    if len(basket) == 0 or basket is None:
        return None

    return basket[0]


async def add_product_to_basket_field(user: str, product_pos):
    selected_basket = await select_user_by_basket(user)
    if not isinstance(selected_basket, dict):
        return (None, "User not find.")

    products_pos = json.loads(selected_basket["product_pos"])


