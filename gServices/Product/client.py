import grpc
from stubs import product_pb2_grpc
from stubs import product_pb2
import _credentials
import logging
import asyncio

_SERVER_ADDR_TEMPLATE = "localhost:%d"
_SIGNATURE_HEADER_KEY = "x-signature"

_LOGGER = logging.getLogger(__name__)


class AuthGateway(grpc.AuthMetadataPlugin):
    def __call__(self, 
                 context: grpc.AuthMetadataContext,
                 callback: grpc.AuthMetadataPluginCallback
                 ) -> None:
        signature = context.method_name[::-1]  # type: ignore
        callback(((_SIGNATURE_HEADER_KEY, signature),), None)


def create_client_channel(addr: str) -> grpc.aio.Channel:
    call_credentials = grpc.metadata_call_credentials(
        AuthGateway(), name="auth gateway"
    )

    channel_credentials = grpc.ssl_channel_credentials(
        _credentials.ROOT_CERTIFICATE
    )

    composite_credentials = grpc.composite_channel_credentials(
        channel_credentials,
        call_credentials
    )

    channel = grpc.aio.secure_channel(addr, composite_credentials)
    return channel


async def send_rpc(channel: grpc.aio.Channel):
    stub = product_pb2_grpc.ProductStub(channel)
    request = product_pb2.ProductListRequest()
    add_request = product_pb2.ProductObject(
        title="Balenciaga",
        description="New shoes",
        price=100.50,
        state=product_pb2.ProductObject.State.DISABLE
    )
    try:
        response = await stub.List(request)
        response_add = await stub.Add(add_request)
    except grpc.RpcError as rpc_error:
        _LOGGER.error("Received error: %s", rpc_error)
        return rpc_error
    else:
        _LOGGER.info("Received message of list: %s", response)
        _LOGGER.info("Received message of add: %s", response_add)
        return response


async def main():
    channel = create_client_channel("localhost:50051")
    await send_rpc(channel)
    await channel.close()

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
