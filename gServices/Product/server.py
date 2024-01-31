from grpc import aio, StatusCode
import grpc
import asyncio
from stubs import product_pb2
from stubs import product_pb2_grpc
import logging

from piccolo.table import create_db_tables
from models import ProductTable

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


class Product(product_pb2_grpc.ProductServicer):
    def __init__(self) -> None:
        pass

    async def List(self, request, context: grpc.ServicerContext):
        products = await ProductTable.select()
        return product_pb2.ProductListResponse(products=products)

    async def Add(self,
                request: product_pb2.ProductObject,
                context: grpc.ServicerContext):
        product = await ProductTable.insert(
            ProductTable(title=request.title,
                         description=request.description,
                         state=request.state,
                         price=request.price)
        )

        return product_pb2.AddProductResponse(product=product[0])

    async def Read(self,
                   request: product_pb2.ReadProductRequest,
                   context: grpc.ServicerContext
                ) -> product_pb2.ReadProductResponse:
        product = await ProductTable.select().where(ProductTable.id == request.product_id).first()
        if not product:
            context.set_code(StatusCode.INVALID_ARGUMENT)
            context.set_details("This product is not defined.")
            return product_pb2.ReadProductResponse()

        return product_pb2.ReadProductResponse(product=product)
    
    async def Delete(self,
                     request: product_pb2.DeleteProductRequest,
                     context: grpc.ServicerContext
                ) -> product_pb2.DeleteProductResponse:
        await ProductTable.delete().where(ProductTable.id == request.product_id)        
        return product_pb2.DeleteProductResponse(success=True)


async def serve(port: int) -> None:
    trace.set_tracer_provider(
        TracerProvider(resource=Resource.create({SERVICE_NAME: "Product"}))
    )

    jaeger_exporter = JaegerExporter(
        collector_endpoint=JAEGER_SERVER_ADDR,
        insecure=True
    )

    # print(jaeger_exporter.export())
    span_processor = BatchSpanProcessor(jaeger_exporter)

    trace.get_tracer_provider().add_span_processor(span_processor)
    grpc_server_instrumentor = GrpcAioInstrumentorServer()
    grpc_server_instrumentor.instrument()
    grpc_client_instrumentor = GrpcAioInstrumentorClient()
    grpc_client_instrumentor.instrument()

    server = aio.server()
    product_pb2_grpc.add_ProductServicer_to_server(
        Product(),
        server)

    port = server.add_insecure_port(
        _LISTEN_ADDRESS_TEMPLATE % port
    )

    logging.info("Server serving at %s port", port)
    await create_db_tables(
        ProductTable, if_not_exists=True
    )

    SERVICE_NAMES = (
        product_pb2.DESCRIPTOR.services_by_name["Product"].full_name,
        reflection.SERVICE_NAME,
    )
    print("\t\t", SERVICE_NAMES)
    reflection.enable_server_reflection(SERVICE_NAMES, server)

    await server.start()
    await server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(serve(50051))
