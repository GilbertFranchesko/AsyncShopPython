from fastapi.testclient import TestClient
import typing as t
from .main import app
from .schemas import ProductModel

client = TestClient(app)

PRODUCT_OBJECT: ProductModel = ProductModel(
    title="string",
    description="I am the testing product",
    price=120.0, state=3
)
ADDED_PRODUCT_ID: t.Optional[int] = 49


def test_ping_pong():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"ping": "pong"}


def test_product_add():
    response = client.post("/products/add", json=PRODUCT_OBJECT.__dict__)
    response_content = response.json()
    ADDED_PRODUCT_ID = response_content.get("product", None).get("id", None)
    assert response.status_code == 200
    assert ADDED_PRODUCT_ID is not None


def test_product_list():
    get_list = client.get("/products/list")
    products_list: list = get_list.json()["products"]
    assert ADDED_PRODUCT_ID is not None
    assert isinstance(products_list, list)

    find_product = None

    for product in products_list:
        if int(product["id"]) == int(ADDED_PRODUCT_ID):
            find_product = product
    assert find_product is not None

    for tmp_product in products_list:
        if tmp_product["title"] == PRODUCT_OBJECT.title:
            product_id = tmp_product["id"]
            response = client.delete(f"/product/{product_id}")
            assert response.status_code == 200


def test_product_get():
    response = client.get(f"/product/get?product_id={ADDED_PRODUCT_ID}")
    print(f"/product/get?product_id={ADDED_PRODUCT_ID}")
    assert response.status_code == 200  # BUG!!! DONT SHOW INFORMATION!!!!


def test_product_delete():
    response = client.delete(f"/product/{ADDED_PRODUCT_ID}")
    assert response.status_code == 200  # EDIT STATIS CODE FOR DELETE!!!
