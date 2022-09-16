# -*- coding: utf-8 -*-
"""
   Description:
        -
        -
"""
from flask_restful import Resource

from schemas.user import UserPackageSchema, UserPackageResponse
from connect import security
from utils import dt_utcnow
from helper.package import get_packages, get_user_packages
from schemas.package import ListPackageResponse

class PackageResource(Resource):

    @security.http(
        # login_required=True
        response=ListPackageResponse()
    )
    def get(self):
        
        _packages = get_packages()    

        return  {"packages": _packages}


    @security.http(
        # form_data=UserPackageSchema(),
        response=UserPackageResponse(),
        login_required=True  # user
    )
    def post(self, user):
        
        _packages = get_user_packages(user.get("_id"))
        _response = {
            "packages": _packages
        }
       
        return _response