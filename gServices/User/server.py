from grpc import aio
import asyncio
from stubs import user_pb2, user_pb2_grpc
import logging

import user as user_utils

from google.protobuf.json_format import MessageToDict

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


class UserService(user_pb2_grpc.UserServiceServicer):
    def __init__(self) -> None:
        pass

    async def Register(self,
                       request: user_pb2.RegisterUserRequest, 
                       context) -> user_pb2.RegisterUserResponse:
        
        request_to_dict = MessageToDict(request)
        register_status = await user_utils.register(**request_to_dict)

        return user_pb2.RegisterUserResponse(created_user=register_status)


async def serve(port: int) -> None:
    trace.set_tracer_provider(
        TracerProvider(resource=Resource.create({SERVICE_NAME: "User"}))
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
    user_pb2_grpc.add_UserServiceServicer_to_server(
        UserService(),
        server)

    port = server.add_insecure_port(
        _LISTEN_ADDRESS_TEMPLATE % port
    )

    logging.info("Server serving at %s port", port)
    await user_utils.db_unit()

    SERVICE_NAMES = (
        user_pb2.DESCRIPTOR.services_by_name["UserService"].full_name,
        reflection.SERVICE_NAME,
    )
    reflection.enable_server_reflection(SERVICE_NAMES, server)

    await server.start()
    await server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(serve(50053))
