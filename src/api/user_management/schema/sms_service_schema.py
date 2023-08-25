from pydantic import BaseModel
from typing import Optional


class SmsInput(BaseModel):
    message: Optional[str]
    number: Optional[int]
