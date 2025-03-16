from pydantic import BaseModel

class advInfoDto(BaseModel):
    number: str
    title: str
    description: str
