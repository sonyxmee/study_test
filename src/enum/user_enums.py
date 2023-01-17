from enum import Enum


class GenderEnum(Enum):
    female = 'female'
    male = 'male'


class StatusEnum(Enum):
    active = 'active'
    inactive = 'inactive'
    delete = 'delete'
    banned = 'banned'


class UserErrorEnum(Enum):
    WRONG_EMAIL = 'email is not contain @.'
