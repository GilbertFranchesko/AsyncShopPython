import typing as t
from google.protobuf.json_format import MessageToDict

"""
    Декоратор множества выводов.
Данный декоратор изпользуется в случае когда функция
возвращает обьект данных из basket_pb2.py или product_pb2.py.
И для типизации и работы корректно с этими данными функция которая обернута
в данный декоратор, будет выводить множество.
1-ым элементом которого является сам обьект из *_pb2.py
2-ым элементом есть обьект возврощаемых данных который указан в
аргументе декоратора.
"""


def mixed_results(out_object: t.Callable, first_key: t.Optional[str] = None):
    def comp_results(func):
        async def wrapper(*args, **kwargs) -> t.Tuple[t.Any, t.Any]:
            """ Получаем результат от функции """
            same_output: t.Any = await func(*args, **kwargs)
            """ Создаём от этого результата обьект с аргумента декоратора """
            if first_key is None:
                init_args = same_output
            else:
                init_args = MessageToDict(getattr(same_output, first_key))

            same_object = out_object(**init_args)

            return same_output, same_object
        return wrapper
    return comp_results
