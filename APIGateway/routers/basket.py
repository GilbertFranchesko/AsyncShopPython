from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse

from ..clients import grpc_basket_client
from ..stubs import basket_pb2, product_pb2
from ..schemas import BasketModel, AddProductBasket

from google.protobuf.json_format import MessageToDict
from grpc.aio._call import AioRpcError

import typing as t

router = APIRouter(
    prefix="/basket",
    tags=["Basket"],
    responses={404: {"description": "Not found"}},
)


@router.get("/basket/list/")
async def basket_list(basket_client: t.Any = Depends(grpc_basket_client)):
    try:
        baskets = await basket_client.List(basket_pb2.ListBasketRequest())
    except AioRpcError as e:
        raise HTTPException(status_code=400, detail=e.details())

    return JSONResponse(MessageToDict(baskets))


@router.post("/basket/addProduct/")
async def add_product_basket(add_basket: AddProductBasket, client: t.Any = Depends(grpc_basket_client)):
    try:
        product = product_pb2.ProductObject(id=add_basket.product_position.product)
        basket = await client.AddProduct(basket_pb2.AddProductRequest(
            user=add_basket.user,
            productPosition=basket_pb2.ProductPosition(product=product, coll=add_basket.product_position.coll)
        ))
    except AioRpcError as e:
        raise HTTPException(status_code=400, detail=e.details())

    return JSONResponse(MessageToDict(basket))
