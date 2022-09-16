
from models import PackageModel, UserPackageModel
from bson import ObjectId
from utils import dt_utcnow
from exception import BadRequest
from datetime import datetime, timezone, timedelta
from config import Config
from dateutil.relativedelta import relativedelta
from lib.logger import debug

def get_packages():
    
    _package = list(PackageModel.find(filter=None))
    return _package



def get_user_packages(user_id):
    debug(f"user_id {user_id}")
    _package = list(UserPackageModel.find(filter={
        "user_id": ObjectId(user_id),
    }))
    
    for package in _package:
        if "valid_until" in package and package["status"] == "active" \
            and package['valid_until'].timestamp() < dt_utcnow().timestamp():
                
            UserPackageModel.update_one(filter={
                "user_id": package['user_id'],
                "package_id": package['package_id'],
                }, obj={
                    "status": "inactive",
                    "updated_by": Config.PROJECT
                })

            _package = list(UserPackageModel.find(filter={
                    "user_id": ObjectId(user_id)
                }))
    return _package



def convert_valid_until(argument):
    print('argument ', argument)
    switch={
      "DAY": relativedelta(days=argument['time']),
      "MONTH": relativedelta(months=argument['time']),
      "YEAR": relativedelta(years=argument['time']),
      }
    return switch.get(argument['unit_time'],"Invalid unit")

def register_package(form_data):
    
    try:
        _package = PackageModel.find_one(filter={
            "_id": ObjectId(form_data['package_id']),
        })
        debug("_package {_package}")

        if not _package:
            raise  BadRequest("Invalid package.")
        
        _valid_until = datetime.utcnow().replace(tzinfo=timezone.utc) + convert_valid_until(_package)
        
        debug("_valid_until {_valid_until}")
        
        _user_package = {
            "user_id": ObjectId(form_data['user_id']),
            "package_id": ObjectId(form_data['package_id']),
            "type": _package.get('type'),
            "status": "active",
            "valid_until":  _valid_until,
            "contract" : None,
            "token_id" : None,
            "created_by": Config.PROJECT
        }
        
        _existing_package = UserPackageModel.find_one(filter={
            "user_id": ObjectId(form_data['user_id']),
            "package_id": ObjectId(form_data['package_id']),
            "valid_until": {
                "$gt": datetime.utcnow()
            }
        })
        debug(f"_existing_package {_existing_package}")
        if _existing_package:

            # update valid_until on case have existing package
            _update = {
                "valid_until":  _existing_package['valid_until'] + convert_valid_until(_package),
                "updated_by": Config.PROJECT
            }
            UserPackageModel.update_one(filter={
            "_id": _existing_package['_id'],
        
        }, obj=_update)
            
        else:
            
            UserPackageModel.insert_one(_user_package)
        
    except Exception as e:
        debug(f"Error {e}")
        raise BadRequest("Register package fail.")