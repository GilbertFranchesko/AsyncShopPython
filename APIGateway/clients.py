from .stubs import product_pb2_grpc, basket_pb2_grpc
from .utils import create_client_channel
from . import settings


async def grpc_product_client() -> product_pb2_grpc.ProductStub:
    channel = await create_client_channel(settings.PRODUCT_SERVICE_ADDR)
    stub = product_pb2_grpc.ProductStub(channel)
    return stub


async def grpc_basket_client() -> basket_pb2_grpc.BasketServiceStub:
    channel = await create_client_channel(settings.BASKET_SERVICE_ADDR)
    return basket_pb2_grpc.BasketServiceStub(channel)
