from pydantic import BaseModel, Field
from typing import List, Any, Optional


class BaseResp(BaseModel):
    code: int = Field(description="状态码")
    message: str = Field(description="信息")
    data: List = Field(description="数据")


class ResAntTable(BaseModel):
    code: int = Field(description="状态码")
    data: List = Field(description="数据")
    total: int = Field(description="总条数")
    message: str = Field(description="信息")
    page: int = Field(description="页码")
    pagesize: int = Field(description="每页展示数据量")
