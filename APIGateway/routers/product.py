from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse

from ..clients import grpc_product_client
from ..stubs import product_pb2
from ..schemas import ProductModel

from google.protobuf.json_format import MessageToDict
from grpc.aio._call import AioRpcError

import typing as t

router = APIRouter(
    prefix="/product",
    tags=["product"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def list_products(client: t.Any = Depends(grpc_product_client)):
    products = await client.List(product_pb2.ProductListRequest())
    return JSONResponse(MessageToDict(products))


@router.post("/")
async def product_add(
        product_object: ProductModel,
        client: t.Any = Depends(grpc_product_client)
     ):

    try:
        product_add = await client.Add(product_object.to_serialize())
    except AioRpcError as e:
        raise HTTPException(status_code=400, detail=e.details())

    return JSONResponse(MessageToDict(product_add))


@router.get("/{product_id:int}")
async def product_get(
        product_id: int,
        client: t.Any = Depends(grpc_product_client)
     ):

    try:
        product = await client.Read(product_pb2.ReadProductRequest(product_id=product_id))
    except AioRpcError as e:
        raise HTTPException(status_code=400, detail=e.details())

    return JSONResponse(MessageToDict(product))


@router.delete("/{product_id:int}")
async def product_delete(product_id: int, client: t.Any = Depends(grpc_product_client)) -> None:
    try:
        await client.Delete(product_pb2.DeleteProductRequest(product_id=product_id))
    except AioRpcError as e:
        raise HTTPException(status_code=400, detail=e.details())
