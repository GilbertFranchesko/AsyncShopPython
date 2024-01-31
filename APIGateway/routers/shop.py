from fastapi import APIRouter
from fastapi.responses import JSONResponse
import typing as t

router = APIRouter(
    prefix="/shop",
    tags=["Shop"],
    responses={404: {"description": "Not found"}},
)


@router.get("/list")
async def list_shops():
    return


@router.post("/auth")
async def authorize_shop():
    return


@router.get("/logout")
async def logout_shop():
    return


@router.post("/create")
async def create_shop():
    pass
