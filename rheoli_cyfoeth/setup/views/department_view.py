from typing import Any
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import viewsets, status
from returns.result import Result, Success, Failure
from returns.pipeline import is_successful

from setup.controllers.department_controller import DepartmentController
from setup.models.department import Department
from setup.serializer import DepartmentSerializer

from rest_framework.permissions import IsAdminUser, IsAuthenticated

class DepartmentView(viewsets.ModelViewSet):
    
    queryset = Department.objects.all();
    serializer_class = DepartmentSerializer
    
    def __init__(self, **kwargs: Any):
        self.controller = DepartmentController()
        
    # Override
    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action == 'destroy':
            permission_classes = [IsAdminUser, IsAuthenticated]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
    
    # Override
    def destroy(self, request: Request, pk=None) -> Response:
        """
        Delete a department by id.
        """
        result = self.controller.delete(pk)
        return Response(status=result.unwrap())
    
    # Override
    def retrieve(self, request: Request, pk=None) -> Response:
        """
        Get a department by id.
        """
        result = self.controller.get_by_id(pk)
        if(not is_successful(result)):
            exception = result.failure()
            return Response(data=exception.message, status=exception.status_code, exception=True) 
        
        return Response(result.unwrap(), status=status.HTTP_200_OK)