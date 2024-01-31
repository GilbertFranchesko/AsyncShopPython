from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import logging
import sqlalchemy as sa

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:product_pass@db:5432/postgres"


class DBExecutor:
    def __init__(self, dsn: str) -> None:
        self._dsn = dsn
        self._base = declarative_base()
        self._engine = create_engine(self._dsn)
        self._session = sessionmaker(bind=self._engine)

    def create_all(self):
        self._base.metadata.drop_all(self._engine)
        self._base.metadata.create_all(self._engine)

    def get_base(self):
        return self._base
    
    def select_all(self, table):
        with self._session() as session:
            return session.query(table).all()

    def get_session(self):
        return self._session()


executor = DBExecutor(SQLALCHEMY_DATABASE_URL)
logging.info("DBExecutor successfully created!")
Base = executor.get_base()


class ProductTable(Base):
    __tablename__ = "products"
    id = sa.Column(sa.Integer(), primary_key=True)
    slug = sa.Column(sa.String(100), nullable=False, unique=True)
    shop_hash = sa.Column(sa.Text(), nullable=False, unique=True)
    title = sa.Column(sa.String(100), nullable=False)
    price = sa.Column(sa.Float(), nullable=False)
    created_on = sa.Column(sa.DateTime(), default=datetime.now)
    updated_on = sa.Column(sa.DateTime(), default=datetime.now, onupdate=datetime.now)
    content = sa.Column(sa.Text())
    state = sa.Column(sa.Integer(), nullable=False)


executor.create_all()


def init_db():
    return executor



#  sa.MetaData()


# products = sa.Table(
#     "products",
#     metadata,
#     sa.Column("id", sa.Integer, primary_key=True),
#     sa.Column("store_hash", sa.String),
#     sa.Column("price", sa.Float),
#     sa.Column("title", sa.String),
#     sa.Column("active", sa.Boolean)
# )


# class AiopgExecutor:
#     engine: aiopg.sa.engine.Engine
#     statement: str

#     def __init__(self, engine):
#         self.engine = engine
#         self.statement = None
#         self.response = None

#     @property
#     def sa_engine(self):
#         return sa.create_engine(
#             SQLALCHEMY_DATABASE_URL
#         )

#     def _compile(self, sql, *multiparams, **params):
#         # pylint: disable=W0613, unused-argument
#         self.statement = str(sql.compile(dialect=self.sa_engine.dialect))

#     async def execute(self):
#         async with self.engine.acquire() as conn:
#             await conn.execute(self.statement)

#     async def same_execute(self, query: Any):
#         async with self.engine.acquire() as conn:
#             response = await conn.execute(query)
#         self.response = response
    
#     def get_response(self):
#         return self.response
    



# async def create_all(engine, metadata):
#     executor = AiopgExecutor(engine)
#     metadata.create_all(executor.sa_engine, checkfirst=False)
#     await executor.execute()


# async def drop_all(engine, metadata):
#     executor = AiopgExecutor(engine)
#     metadata.drop_all(executor.sa_engine, checkfirst=False)
#     await executor.execute()


# async def init_db():
#     async with create_engine(SQLALCHEMY_DATABASE_URL) as engine:
#         # await drop_all(SQLALCHEMY_DATABASE_URL, metadata)
#         try:
#             await create_all(engine, metadata)
#         except Exception as e:
#             print(e)

#         return AiopgExecutor(engine)
