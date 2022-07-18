# 视图基础路由

from fastapi import APIRouter, Request, Cookie
from fastapi.templating import Jinja2Templates
from config import settings
from starlette.responses import HTMLResponse
from typing import Optional

View_Router = APIRouter(prefix="/view", tags=["视图路由"])

templates = Jinja2Templates(directory=settings.STATIC_DIR + "/templates")


@View_Router.get("/item/{id}", response_class=HTMLResponse, summary="视图测试", deprecated=True)
async def read_item(request: Request, id: str):
    return templates.TemplateResponse("index.html", {"request": request, "id": id})


@View_Router.get("/home", response_class=HTMLResponse, summary="视图测试cookie、session", deprecated=True)
async def home(request: Request, session_id: Optional[str] = Cookie(None)):
    cookie = session_id
    session = request.session.get("session")
    page_data = {
        "cookie": cookie,
        "session": session
    }
    print(page_data)
    return templates.TemplateResponse("index.html", {"request": request, **page_data})
