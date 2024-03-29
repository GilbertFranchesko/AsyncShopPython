# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import product_pb2 as product__pb2


class ProductStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.List = channel.unary_unary(
                '/product.Product/List',
                request_serializer=product__pb2.ProductListRequest.SerializeToString,
                response_deserializer=product__pb2.ProductListResponse.FromString,
                )
        self.Add = channel.unary_unary(
                '/product.Product/Add',
                request_serializer=product__pb2.ProductObject.SerializeToString,
                response_deserializer=product__pb2.AddProductResponse.FromString,
                )
        self.Edit = channel.unary_unary(
                '/product.Product/Edit',
                request_serializer=product__pb2.EditProductRequest.SerializeToString,
                response_deserializer=product__pb2.EditProductResponse.FromString,
                )
        self.Delete = channel.unary_unary(
                '/product.Product/Delete',
                request_serializer=product__pb2.DeleteProductRequest.SerializeToString,
                response_deserializer=product__pb2.DeleteProductResponse.FromString,
                )
        self.Read = channel.unary_unary(
                '/product.Product/Read',
                request_serializer=product__pb2.ReadProductRequest.SerializeToString,
                response_deserializer=product__pb2.ReadProductResponse.FromString,
                )


class ProductServicer(object):
    """Missing associated documentation comment in .proto file."""

    def List(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Add(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Edit(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Delete(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Read(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ProductServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'List': grpc.unary_unary_rpc_method_handler(
                    servicer.List,
                    request_deserializer=product__pb2.ProductListRequest.FromString,
                    response_serializer=product__pb2.ProductListResponse.SerializeToString,
            ),
            'Add': grpc.unary_unary_rpc_method_handler(
                    servicer.Add,
                    request_deserializer=product__pb2.ProductObject.FromString,
                    response_serializer=product__pb2.AddProductResponse.SerializeToString,
            ),
            'Edit': grpc.unary_unary_rpc_method_handler(
                    servicer.Edit,
                    request_deserializer=product__pb2.EditProductRequest.FromString,
                    response_serializer=product__pb2.EditProductResponse.SerializeToString,
            ),
            'Delete': grpc.unary_unary_rpc_method_handler(
                    servicer.Delete,
                    request_deserializer=product__pb2.DeleteProductRequest.FromString,
                    response_serializer=product__pb2.DeleteProductResponse.SerializeToString,
            ),
            'Read': grpc.unary_unary_rpc_method_handler(
                    servicer.Read,
                    request_deserializer=product__pb2.ReadProductRequest.FromString,
                    response_serializer=product__pb2.ReadProductResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'product.Product', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Product(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def List(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/product.Product/List',
            product__pb2.ProductListRequest.SerializeToString,
            product__pb2.ProductListResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Add(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/product.Product/Add',
            product__pb2.ProductObject.SerializeToString,
            product__pb2.AddProductResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Edit(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/product.Product/Edit',
            product__pb2.EditProductRequest.SerializeToString,
            product__pb2.EditProductResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Delete(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/product.Product/Delete',
            product__pb2.DeleteProductRequest.SerializeToString,
            product__pb2.DeleteProductResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Read(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/product.Product/Read',
            product__pb2.ReadProductRequest.SerializeToString,
            product__pb2.ReadProductResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
