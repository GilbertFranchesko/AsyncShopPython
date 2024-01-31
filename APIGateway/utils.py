import grpc


async def create_client_channel(addr: str) -> grpc.aio.Channel:
    channel = grpc.aio.insecure_channel(addr)
    return channel
