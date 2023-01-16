from pydantic import validator, BaseModel, Field


class Post(BaseModel):
    id: int = Field(gt=0)
    title: str
    # name: str = Field(alias='_name')
    # {'id': 1, 'title': 'Post 1'}

    # @validator('id')
    # def custom_validator(cls, v):
    #     if v < 0:
    #         raise ValueError('Id is not gather than zero')
    #     else:
    #         return v