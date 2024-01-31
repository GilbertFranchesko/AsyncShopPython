from models import UserTable
from schemas import User, isinstance_model
from piccolo.table import create_db_tables
import typing as t
from hashlib import md5

async def db_unit():
    await create_db_tables(UserTable, if_not_exists=True)


async def register(*args, **kwargs) -> t.Optional[User]:
    isinstance_model(User, kwargs)
    
    first_name = kwargs['firstName']
    last_name = kwargs['lastName']
    email = kwargs['email']
    password = kwargs['password']

    check_user = await search_user(email)

    if check_user is not None:
        raise Exception("Error", "Email is already created.")

    hash_password = md5(password.encode("utf-8")).hexdigest()

    created_user = await UserTable.insert(
        UserTable(
            first_name = first_name,
            last_name = last_name,
            email=email,
            password=hash_password
    ))

    print(created_user)


    return created_user[0]


async def login():
    pass


async def checking_exists_user(email: str) -> bool:
    some_user = await UserTable.select().where(UserTable.email == email)
    if len(some_user) != 0 or some_user[0] is not None:
        return True
    
    return False


async def create_token(email: str, password: str):
    pass

async def search_user(email: str):
    some_user = await UserTable.select().where(UserTable.email == email)
    if len(some_user) == 0 or some_user is None:
        return None

    return some_user[0]