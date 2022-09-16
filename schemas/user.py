# -*- coding: utf-8 -*-
"""
   Description:
        -
        -
"""
from marshmallow import Schema, EXCLUDE, RAISE, fields
from schemas.base import NotBlank, IsObjectId, ResDatetimeField

class UserPackageSchema(Schema):
    class Meta:
        unknown = RAISE

    user_id = fields.Str(required=True, validate=IsObjectId())


class UserRegisterPackageSchema(Schema):
    class Meta:
        unknown = RAISE

    # user_id = fields.Str(required=True, validate=IsObjectId())
    package_id = fields.Str(required=True, validate=IsObjectId())


class PackageItemResponse(Schema):
    class Meta:
        unknown = EXCLUDE

    type = fields.Str()
    status = fields.Str()
    valid_until = ResDatetimeField()
    contract = fields.Str(required=False, missing=None)
    token_id = fields.Str(required=False, missing=None)
    created_time = ResDatetimeField()


class UserPackageResponse(Schema):
    class Meta:
        unknown = RAISE

    # user_id = fields.Str(required=True, validate=IsObjectId())
    packages = fields.List(fields.Nested(PackageItemResponse))

