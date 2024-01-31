from contextlib import contextmanager
import unittest
import grpc

from concurrent import futures
from server import BasketService
from stubs import basket_pb2_grpc, basket_pb2

from stubs import product_pb2, product_pb2_grpc
from google.protobuf.json_format import MessageToDict

def great(text):
    print(text)


@contextmanager
def basket(cls):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    basket_pb2_grpc.add_BasketServiceServicer_to_server(cls(), server)
    server.start()

    try:
        with grpc.insecure_channel('localhost:50052') as channel:
            yield basket_pb2_grpc.BasketServiceStub(channel)
        
    finally:
        server.stop(None)

class BasketTests(unittest.TestCase):

    def test_list_baskets(self):
        with basket(BasketService) as stub:
            response = MessageToDict(stub.List(basket_pb2.ListBasketRequest()))
            great(response)
            self.assertTrue(response, dict)
            self.assertTrue(response['baskets'], list)


    def test_add_product(self):
        productPosition = basket_pb2.ProductPosition(
            product=product_pb2.ProductObject(
                id=413
            ),
            coll=2
        )


        with basket(BasketService) as stub:
            response = MessageToDict(
                stub.AddProduct(basket_pb2.AddProductRequest(
                    user="vladhalaburda",
                    productPosition=productPosition
            )))

            great(response)
            self.assertTrue(isinstance(response, dict))
            self.assertTrue(isinstance(response['basket']['id'], int))





if __name__ == '__main__':
    unittest.main()