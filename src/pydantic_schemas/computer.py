from pydantic import BaseModel
from pydantic.types import PastDate, FutureDate
from pydantic.networks import IPv4Address, IPv6Address
from src.enum.user_enums import StatusEnum
from example import computer
from src.pydantic_schemas.detailedinfo import DetailedInfo


class Computer(BaseModel):
    status: StatusEnum
    activated_at: PastDate
    expiration_at: FutureDate
    host_v4: IPv4Address
    host_v6: IPv6Address
    detailed_info: DetailedInfo


comp = Computer.parse_obj(computer)
print(comp.detailed_info.physical.color.as_hsl())
