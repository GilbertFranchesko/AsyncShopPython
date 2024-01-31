import typing as t
import logging
from fastapi import FastAPI
from .routers import product, basket, user, shop

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

app = FastAPI()
app.include_router(user.router)
app.include_router(shop.router)

app.include_router(product.router)
app.include_router(basket.router)


@app.get("/")
async def ping():
    return {"ping": "pong"}
