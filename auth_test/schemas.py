from pydantic import BaseModel


class AuthDetails(BaseModel):
    username: str
    hashed_password: str


class DataPayload(BaseModel):
    company_id: int
    roles: list
    scope: list
