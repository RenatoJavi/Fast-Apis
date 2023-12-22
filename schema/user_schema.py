from pydantic import BaseModel
from typing import Optional

# que datos tengo en mi bd?
class UserSchema(BaseModel):
    id: Optional[int]
    name:str
    phone:str
    