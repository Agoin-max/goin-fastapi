from fastapi import Request, HTTPException, status


# PHP交互
async def check_authorization(req: Request):
    authorization: str = req.headers.get("Authorization")
    if not authorization:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not authenticated",
            headers=None
        )
