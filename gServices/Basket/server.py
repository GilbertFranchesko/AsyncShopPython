from grpc import aio, StatusCode
import grpc
import asyncio
from stubs import basket_pb2 as b_pb2
from stubs import basket_pb2_grpc as b_pb2_grpc
import logging
import basket as b_utils

from grpc_reflection.v1alpha import reflection

from opentelemetry import trace
from opentelemetry.instrumentation.grpc import (
    GrpcAioInstrumentorServer,
    GrpcAioInstrumentorClient,
)
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.jaeger.proto.grpc import JaegerExporter
from opentelemetry.sdk.resources import SERVICE_NAME, Resource


JAEGER_SERVER_ADDR = "jeager_service:14250"


_LISTEN_ADDRESS_TEMPLATE = "[::]:%d"


class BasketService(b_pb2_grpc.BasketServiceServicer):
    def __init__(self) -> None:
        pass

    async def AddProduct(
            self,
            request: b_pb2.AddProductRequest,
            context: grpc.aio.ServicerContext) -> b_pb2.AddProductResponse:

        basket = await b_utils.init_basket(request.user, request.productPosition)
        if basket is None:
            context.set_code(StatusCode.INVALID_ARGUMENT)
            context.set_details("This basket is too defined by this user.")
            return b_pb2.AddProductResponse()

        return b_pb2.AddProductResponse(basket=basket)

    async def List(
            self,
            request: b_pb2.ListBasketRequest,
            context: grpc.aio.ServicerContext) -> b_pb2.ListBasketResponse:
        baskets = await b_utils.list_of_basket()
        print(baskets)
        return b_pb2.ListBasketResponse(baskets=baskets)


async def serve(port: int) -> None:
    trace.set_tracer_provider(
        TracerProvider(resource=Resource.create({SERVICE_NAME: "Basket"}))
    )

    jaeger_exporter = JaegerExporter(
        collector_endpoint=JAEGER_SERVER_ADDR,
        insecure=True
    )

    # print(jaeger_exporter.export())
    span_processor = BatchSpanProcessor(jaeger_exporter)

    trace.get_tracer_provider().add_span_processor(span_processor)  # type: ignore
    grpc_server_instrumentor = GrpcAioInstrumentorServer()
    grpc_server_instrumentor.instrument()
    grpc_client_instrumentor = GrpcAioInstrumentorClient()
    grpc_client_instrumentor.instrument()

    server = aio.server()
    b_pb2_grpc.add_BasketServiceServicer_to_server(
        BasketService(),
        server)

    port = server.add_insecure_port(
        _LISTEN_ADDRESS_TEMPLATE % port
    )

    logging.info("Server serving at %s port", port)
    await b_utils.db_unit()

    SERVICE_NAMES = (
        b_pb2.DESCRIPTOR.services_by_name["BasketService"].full_name,
        reflection.SERVICE_NAME,
    )
    reflection.enable_server_reflection(SERVICE_NAMES, server)

    await server.start()
    await server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(serve(50052))
