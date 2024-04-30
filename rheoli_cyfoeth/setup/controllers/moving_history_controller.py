import datetime
from typing import List, Tuple
from returns.result import Result, Success, Failure

from setup.models.department import Department
from setup.models.item import Item
from setup.models.moving_history import MovingHistory
from ..utils.models_utils.custom_exception import CustomException
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.request import Request
from setup.utils.response_utils import ResponseUtils
from setup.utils.validation_utils import ValidationUtils
from rest_framework.serializers import ReturnDict

class MovingHistoryController:
    
    def create(self, data: ReturnDict) -> Result[MovingHistory, CustomException]:
        
            try:
                validation = self.__validate_create(data)
                if(validation is CustomException):
                    return Failure(validation)
                
                (initial_department, destination_department) = validation
                
                result = MovingHistory.objects.create(
                    start_date=data['start_date'],
                    finish_date=data['finish_date'],
                    initial_department=initial_department,
                    destination_department=destination_department,
                    item_id=data['item_id']
                )
                
                item = Item.objects.get(id=result.item_id)
                item.moving_history.add(result)
                item.department = destination_department
                item.save()
                
                return Success(result)
            except Exception as e:
                return Failure(CustomException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, message={'detail': str(e)}))
    
    def __validate_create(self,data: ReturnDict) -> Tuple | CustomException:
       try:
         dateformat = '%y-%m-%dT%H:%M:%SZ'
         item = Item.objects.get(id=data['item_id'])
         allmovings = item.moving_history.all()
         conflict = [moving for moving in allmovings if (moving.finish_date == datetime.datetime.fromisoformat(data['finish_date']))]
         if(len(conflict) > 0):
             return ResponseUtils.invalid_data_error_data(text= 'Conflict with another moving')
         
         initial_department = Department.objects.get(id=data['initial_department'])
         destination_department = Department.objects.get(id=data['destination_department'])
         
         return (initial_department, destination_department)
        
       except Item.DoesNotExist:
           return ResponseUtils.invalid_data_error_data(text= 'Invalid Item')
       except Department.DoesNotExist:
           return ResponseUtils.invalid_data_error_data(text= 'Invalid Department')
       except Exception as e:
           return CustomException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, message={'detail': str(e)})