from pydantic import BaseModel
import typing as t


class User(BaseModel):
    id: int
    firstName: str
    lastName: str
    email: str
    password: str


def isinstance_model(cls, data: dict):
    fields = cls.model_fields
    for field in fields.keys():
        if data.get(field, None) is None:
            if field == "id":
                continue
            raise Exception("{} have not {}".format(data, field))



