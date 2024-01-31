from contextlib import contextmanager
import unittest
import grpc

from concurrent import futures
from server import UserService
from stubs import user_pb2, user_pb2_grpc

from google.protobuf.json_format import MessageToDict

def great(text):
    print(text)


@contextmanager
def user(cls):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    user_pb2_grpc.add_UserServiceServicer_to_server(cls(), server)
    server.start()

    try:
        with grpc.insecure_channel('localhost:50053') as channel:
            yield user_pb2_grpc.UserServiceStub(channel)
        
    finally:
        server.stop(None)

class UserTests(unittest.TestCase):
    
    def test_register_user(self):
        with user(UserService) as stub:
            response = stub.Register(user_pb2.RegisterUserRequest(
                first_name="Vlad",
                last_name="Halaburda",
                email="vladgalaburdadevw@gmail.com",
                password="123321"
            ))

            response_dict = MessageToDict(response)
            great(response_dict)


if __name__ == '__main__':
    unittest.main()