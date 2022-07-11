# 入口路由分发

from api.url import Api_Router
from fastapi import APIRouter
from views.Base import View_Router


All_Router = APIRouter()
#  API路由
All_Router.include_router(Api_Router)
#  视图路由
All_Router.include_router(View_Router)
