from pydantic import BaseModel, HttpUrl, UUID4, EmailStr
from pydantic.types import PastDate, FutureDate, List, PaymentCardNumber
from pydantic.networks import IPv4Address, IPv6Address
from pydantic.color import Color
from src.enum.user_enums import StatusEnum
class Physical(BaseModel):
    color: Color
    photo: HttpUrl
    uuid: UUID4