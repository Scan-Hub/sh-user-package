# -*- coding: utf-8 -*-
"""
   Description:
        -
        -
"""
from resources.health_check import HealthCheck
from resources.package import PackageResource
from resources.register import RegisterPackageResource
from resources.iapi import iapi_resources

api_resources = {
    '/': PackageResource,
    '/register': RegisterPackageResource,
    '/common/health_check': HealthCheck,
    **{f'/iapi{k}': val for k, val in iapi_resources.items()}
}
