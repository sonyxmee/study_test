from enum import Enum


class PyEnum(Enum):
    @classmethod
    def get_status_list(cls):
        return list(map(lambda i: i.value, cls))
