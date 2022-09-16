# -*- coding: utf-8 -*-
"""
   Description:
        -
        -
"""
from datetime import datetime, timezone
from bson import ObjectId

def dt_utcnow():
    return datetime.utcnow().replace(tzinfo=timezone.utc)


def is_oid(oid: str) -> bool:
    return ObjectId.is_valid(oid)

