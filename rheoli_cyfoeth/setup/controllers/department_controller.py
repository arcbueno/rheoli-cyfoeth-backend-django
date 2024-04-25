from returns.result import Result, Success, Failure
from rest_framework import status

from setup.models.department import Department

class DepartmentController:
    
    def delete(self, id: int | None) -> Result[int,int]:
        try:
            if(id == None): 
                return Failure(status=status.HTTP_404_NOT_FOUND)
            department = Department.objects.get(id=id)
            department.delete()
            return Success(status=status.HTTP_204_NO_CONTENT)
        except Department.DoesNotExist:
            return Failure(status=status.HTTP_204_NO_CONTENT)
    
    def get_by_id(self, id: int | None) -> Result[Department, int]:
        try:
            if(id == None): 
                return Failure(status=status.HTTP_404_NOT_FOUND)
            department = Department.objects.filter(id=id).prefetch_related('manager').first()
            return Success(department)
        except Department.DoesNotExist:
            return Failure(status=status.HTTP_404_NOT_FOUND)
        except:
            return Failure(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        