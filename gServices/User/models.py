from piccolo.table import Table
from piccolo.columns import Varchar, JSON, Float
from piccolo_conf import DB

class UserTable(Table, db=DB):
    first_name = Varchar(default=None)
    last_name = Varchar(default=None)
    email = Varchar()
    password = Varchar()