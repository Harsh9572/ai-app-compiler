from pydantic import BaseModel
from typing import List


class Page(BaseModel):
    name: str
    route: str


class Table(BaseModel):
    name: str
    columns: List[str]


class Endpoint(BaseModel):
    path: str
    method: str


class Role(BaseModel):
    name: str
    permissions: List[str]


class AppSchema(BaseModel):

    app_name: str

    pages: List[Page]

    tables: List[Table]

    endpoints: List[Endpoint]

    roles: List[Role]

    business_rules: List[str]