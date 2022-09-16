# -*- coding: utf-8 -*-
"""
   Description:
        -
        -
"""
from flask_restful import Resource

from schemas.user import UserRegisterPackageSchema
from connect import security
from helper.package import register_package


class RegisterPackageResource(Resource):

    @security.http(
        form_data=UserRegisterPackageSchema(),  # form_data
        login_required=True  # user
    )
    def post(self, form_data, user):
        form_data['user_id'] = user.get('_id')
        register_package(form_data)
        
        return {}