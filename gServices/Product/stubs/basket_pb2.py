# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: basket.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import product_pb2 as product__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0c\x62\x61sket.proto\x12\x06\x62\x61sket\x1a\rproduct.proto\"H\n\x0fProductPosition\x12\'\n\x07product\x18\x01 \x01(\x0b\x32\x16.product.ProductObject\x12\x0c\n\x04\x63oll\x18\x02 \x01(\x04\"d\n\x06\x42\x61sket\x12\n\n\x02id\x18\x01 \x01(\x04\x12\x0c\n\x04user\x18\x02 \x01(\t\x12\x31\n\x10productsPosition\x18\x03 \x03(\x0b\x32\x17.basket.ProductPosition\x12\r\n\x05price\x18\x04 \x01(\x02\"U\n\x13\x43reateBasketRequest\x12\x0c\n\x04user\x18\x01 \x01(\t\x12\x30\n\x0fproductPosition\x18\x02 \x01(\x0b\x32\x17.basket.ProductPosition\"6\n\x14\x43reateBasketResponse\x12\x1e\n\x06\x62\x61sket\x18\x01 \x01(\x0b\x32\x0e.basket.Basket\"\x13\n\x11ListBasketRequest\"5\n\x12ListBasketResponse\x12\x1f\n\x07\x62\x61skets\x18\x01 \x03(\x0b\x32\x0e.basket.Basket\"S\n\x11\x41\x64\x64ProductRequest\x12\x0c\n\x04user\x18\x01 \x01(\t\x12\x30\n\x0fproductPosition\x18\x02 \x01(\x0b\x32\x17.basket.ProductPosition\"4\n\x12\x41\x64\x64ProductResponse\x12\x1e\n\x06\x62\x61sket\x18\x01 \x01(\x0b\x32\x0e.basket.Basket\"?\n\x14RemoveProductRequest\x12\'\n\x07product\x18\x01 \x01(\x0b\x32\x16.product.ProductObject\"7\n\x15RemoveProductResponse\x12\x1e\n\x06\x62\x61sket\x18\x01 \x01(\x0b\x32\x0e.basket.Basket2\xa6\x02\n\rBasketService\x12\x43\n\x06\x43reate\x12\x1b.basket.CreateBasketRequest\x1a\x1c.basket.CreateBasketResponse\x12=\n\x04List\x12\x19.basket.ListBasketRequest\x1a\x1a.basket.ListBasketResponse\x12\x43\n\nAddProduct\x12\x19.basket.AddProductRequest\x1a\x1a.basket.AddProductResponse\x12L\n\rRemoveProduct\x12\x1c.basket.RemoveProductRequest\x1a\x1d.basket.RemoveProductResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'basket_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_PRODUCTPOSITION']._serialized_start=39
  _globals['_PRODUCTPOSITION']._serialized_end=111
  _globals['_BASKET']._serialized_start=113
  _globals['_BASKET']._serialized_end=213
  _globals['_CREATEBASKETREQUEST']._serialized_start=215
  _globals['_CREATEBASKETREQUEST']._serialized_end=300
  _globals['_CREATEBASKETRESPONSE']._serialized_start=302
  _globals['_CREATEBASKETRESPONSE']._serialized_end=356
  _globals['_LISTBASKETREQUEST']._serialized_start=358
  _globals['_LISTBASKETREQUEST']._serialized_end=377
  _globals['_LISTBASKETRESPONSE']._serialized_start=379
  _globals['_LISTBASKETRESPONSE']._serialized_end=432
  _globals['_ADDPRODUCTREQUEST']._serialized_start=434
  _globals['_ADDPRODUCTREQUEST']._serialized_end=517
  _globals['_ADDPRODUCTRESPONSE']._serialized_start=519
  _globals['_ADDPRODUCTRESPONSE']._serialized_end=571
  _globals['_REMOVEPRODUCTREQUEST']._serialized_start=573
  _globals['_REMOVEPRODUCTREQUEST']._serialized_end=636
  _globals['_REMOVEPRODUCTRESPONSE']._serialized_start=638
  _globals['_REMOVEPRODUCTRESPONSE']._serialized_end=693
  _globals['_BASKETSERVICE']._serialized_start=696
  _globals['_BASKETSERVICE']._serialized_end=990
# @@protoc_insertion_point(module_scope)
