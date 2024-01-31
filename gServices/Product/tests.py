from contextlib import contextmanager
import unittest
import grpc

from concurrent import futures
from server import Product
from stubs import product_pb2, product_pb2_grpc
from google.protobuf.json_format import MessageToDict


@contextmanager
def product(cls):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    product_pb2_grpc.add_ProductServicer_to_server(cls(), server)
    server.start()

    try:
        with grpc.insecure_channel('localhost:50051') as channel:
            yield product_pb2_grpc.ProductStub(channel)
        
    finally:
        server.stop(None)

class ProductTest(unittest.TestCase):

    def test_add_product(self):
        with(product(Product)) as stub:
            response = MessageToDict(stub.Add(product_pb2.ProductObject(
                title="Testing Product",
                description="Testing Description",
                price=25.1,
                state=product_pb2.ProductObject.State.ACTIVE
            )))

            self.assertTrue(isinstance(response, dict))
            self.assertTrue(isinstance(response['product'], dict))


    def test_list_products(self):                       
        with product(Product) as stub:
            response = MessageToDict(stub.List(product_pb2.ProductListRequest()))
            self.assertTrue(isinstance(response, dict))
            self.assertTrue(isinstance(response['products'], list))

            
    def test_delete_products(self):
        with product(Product) as stub:
            products_list = MessageToDict(stub.List(product_pb2.ProductListRequest()))
            delete_product_id = len(products_list)
            response = MessageToDict(stub.Delete(product_pb2.DeleteProductRequest(product_id=delete_product_id)))

            self.assertTrue(isinstance(response, dict))
            self.assertTrue(response['success'] == True)
    
    def test_update_product(self):
        with product(Product) as stub:
            products_list = MessageToDict(stub.List(product_pb2.ProductListRequest()))
            read_product_id = int(products_list['products'][0]['id'])
            response = MessageToDict(stub.Read(product_pb2.ReadProductRequest(product_id=read_product_id)))
            self.assertTrue(response['product'] is not None)




if __name__ == '__main__':
    unittest.main()