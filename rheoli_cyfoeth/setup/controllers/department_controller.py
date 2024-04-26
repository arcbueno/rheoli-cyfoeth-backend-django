from returns.result import Result, Success, Failure
from rest_framework import status

from setup.models.department import Department
from setup.utils.models_utils.custom_exception import CustomException
from setup.utils.response_utils import ResponseUtils

class DepartmentController:
    
    def delete(self, id: int | None) -> Result[int,CustomException]:
        try:
            if(id == None): 
                return Success(status.HTTP_204_NO_CONTENT)
            department = Department.objects.get(id=id)
            department.delete()
            return Success(status.HTTP_204_NO_CONTENT)
        except Department.DoesNotExist:
            return Success(status.HTTP_204_NO_CONTENT)
    
    def get_by_id(self, id: int | None) -> Result[Department, CustomException]:
        try:
            if(id == None): 
                return Failure(ResponseUtils.not_found_error_data(name='Department'))
            department = Department.objects.filter(id=id).prefetch_related('manager').first()
            return Success(department)
        except Department.DoesNotExist:
            return Failure(ResponseUtils.not_found_error_data(name='Department'))
        