from piccolo.table import Table
from piccolo.columns import Varchar, Float, Integer
from piccolo_conf import DB


class ProductTable(Table, db=DB):
    title = Varchar()
    description = Varchar()
    price = Float()
    state = Integer()
