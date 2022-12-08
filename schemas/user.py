from pydantic import BaseModel, Field, validator
from typing import Optional, List

from schemas.base import BaseResp, ResAntTable
from datetime import datetime


class CreateUser(BaseModel):
    username: str = Field(min_length=3, max_length=10)
    password: str = Field(min_length=6, max_length=32)
    user_phone: Optional[str] = Field(regex="^1[34567890]\\d{9}$")
    user_status: Optional[bool]
    remarks: Optional[str]
    roles: Optional[List[int]]


class UpdateUser(BaseModel):
    id: int
    username: Optional[str] = Field(min_length=3, max_length=10)
    password: Optional[str] = Field(min_length=6, max_length=32)
    user_phone: Optional[str] = Field(regex="^1[34567890]\\d{9}$")
    user_status: Optional[bool]
    remarks: Optional[str]


class SetRole(BaseModel):
    user_id: int
    roles: Optional[List[int]] = Field(default=[], description="角色")


class AccessToken(BaseModel):
    token: Optional[str]
    expires_in: Optional[int]


class UserLogin(BaseResp):
    data: AccessToken


class AccountLogin(BaseModel):
    username: Optional[str] = ""
    password: Optional[str] = ""
    mobile: Optional[str] = ""
    captcha: Optional[str] = ""


class UserListItem(BaseModel):
    key: int
    id: int
    username: str
    age: Optional[int]
    user_type: bool
    nickname: Optional[str]
    user_phone: Optional[str]
    user_email: Optional[str]
    full_name: Optional[str]
    user_status: bool
    header_img: Optional[str]
    sex: int
    remarks: Optional[str]
    create_time: datetime
    update_time: datetime


class UserInfo(BaseModel):
    username: str
    age: Optional[int]
    user_type: bool
    nickname: Optional[str]
    user_phone: Optional[str]
    user_email: Optional[str]
    full_name: Optional[str]
    scopes: Optional[List[str]]
    user_status: bool
    header_img: Optional[str]
    sex: int


class UserListData(ResAntTable):
    data: List[UserListItem]


class CurrentUser(BaseResp):
    data: UserInfo


class UpdateUserInfo(BaseModel):
    nickname: Optional[str]
    user_email: Optional[str]
    header_img: Optional[str]
    user_phone: Optional[str] = Field(regex="^1[34567890]\\d{9}$", description="手机号")
    password: Optional[str] = Field(min_length=6, max_length=12, description="密码")

    @validator('*')
    def blank_strings(cls, v):
        if v == "":
            return None
        return v


class ModifyMobile(BaseModel):
    mobile: str = Field(regex="^1[34567890]\\d{9}$", description="手机号")
    captcha: str = Field(min_length=6, max_length=6, description="6位验证码")