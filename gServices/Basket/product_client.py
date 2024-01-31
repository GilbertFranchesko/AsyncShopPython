import grpc
from stubs import product_pb2_grpc

PRODUCT_SERVICE_ADDR = "product_microservice:50051"


async def product_stub():
    channel = grpc.aio.insecure_channel(PRODUCT_SERVICE_ADDR)
    stub = product_pb2_grpc.ProductStub(channel)
    return stub
