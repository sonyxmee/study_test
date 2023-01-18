from enum import Enum
from src.baseclass.pyenum import PyEnum


class GenderEnum(Enum):
    female = 'female'
    male = 'male'


class StatusEnum(PyEnum):
    active = 'active'
    inactive = 'inactive'
    delete = 'delete'
    banned = 'banned'


class UserErrorEnum(Enum):
    WRONG_EMAIL = 'email is not contain @.'
