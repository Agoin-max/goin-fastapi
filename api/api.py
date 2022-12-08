from fastapi import APIRouter

from api.endpoints import user, role, access
from api.extends import sms

api_router = APIRouter(prefix="/api/v1")

api_router.include_router(user.router, prefix='/admin', tags=['用户管理'])
api_router.include_router(role.router, prefix='/admin', tags=["角色管理"])
api_router.include_router(access.router, prefix='/admin', tags=["权限管理"])
api_router.include_router(sms.router, prefix='/sms', tags=["短信接口"])
