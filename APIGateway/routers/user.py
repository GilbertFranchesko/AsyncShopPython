from fastapi import APIRouter
from fastapi.responses import JSONResponse
import typing as t

from ..schemas import UserModel, UserRegisterRequest, AuthRequest

router = APIRouter(
    prefix="/user",
    tags=["User"],
    responses={404: {"description": "Not found"}},
)


@router.get("/list")
async def list_shops() -> t.List[UserModel]:
    return [UserModel(), ]


@router.post("/auth")
async def authorize_shop(auth_params: AuthRequest) -> UserModel:
    return UserModel()


@router.get("/logout")
async def logout_shop():
    return


@router.post("/register")
async def create_shop(register_params: UserRegisterRequest) -> UserModel:
    return UserModel()

