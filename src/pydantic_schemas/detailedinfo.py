from pydantic import BaseModel
from pydantic.types import List
from src.pydantic_schemas.physical import Physical
from src.pydantic_schemas.owners import Owners


class DetailedInfo(BaseModel):
    physical: Physical
    owners: List[Owners]
