# -*- coding: utf-8 -*-
"""
   Description:
        -
        -
"""
from marshmallow import Schema, EXCLUDE, RAISE, fields
from schemas.base import NotBlank, IsObjectId, ResDatetimeField, ObjectIdField

class PackageResponse(Schema):
    class Meta:
        unknown = EXCLUDE
    _id = ObjectIdField()
    type = fields.Str()
    description = fields.Str()
    permission = fields.List(fields.Str())
    price = fields.Float(required=False, allow_none=True, default=0)
    unit_currency = fields.Str(required=False, missing=None)
    unit_timestamp = fields.Str(required=False, missing=None)
 

class ListPackageResponse(Schema):
    class Meta:
        unknown = EXCLUDE

    packages = fields.List(fields.Nested(PackageResponse))
  
 

