# 入口路由分发
from api.api import api_router
from fastapi import APIRouter

all_router = APIRouter()
#  API路由
all_router.include_router(api_router)
