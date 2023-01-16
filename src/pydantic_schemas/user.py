from pydantic import BaseModel, validator
from src.enum.user_enums import GenderEnum, StatusEnum, UserErrorEnum


class User(BaseModel):
    # если полю присвоить значение, то оно может быть необязательным
    id: int
    name: str
    email: str
    gender: GenderEnum
    status: StatusEnum

    @validator('email')
    def check_dog_email(cls, email):
        if '@' in email:
            return email
        else:
            raise ValueError(UserErrorEnum.WRONG_EMAIL.value)
