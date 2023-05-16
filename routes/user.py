from fastapi import APIRouter, Request, Response
from fastapi.responses import JSONResponse

router = APIRouter()

@router.get('/user')
async def get_user(req=Request, res=Response):
    return JSONResponse({'status': True})
