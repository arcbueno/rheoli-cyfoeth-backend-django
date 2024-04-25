from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.decorators import action

from setup.models.department import Department
from setup.serializer import DepartmentSerializer

from rest_framework.permissions import IsAdminUser, IsAuthenticated

class DepartmentView(viewsets.ModelViewSet):
    
    queryset = Department.objects.all();
    serializer_class = DepartmentSerializer
    
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
        try:
            if(pk == None): 
                return Response(status=status.HTTP_404_NOT_FOUND)
            department = Department.objects.get(id=pk)
            Department.delete(department)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Department.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
    def retrieve(self, request: Request, pk=None) -> Response:
        """
        Get a department by id.
        """
        try:
            if(pk == None): 
                return Response(status=status.HTTP_404_NOT_FOUND)
            department = Department.objects.filter(id=pk).prefetch_related('manager').first()
            serialized = DepartmentSerializer(department)
            return Response(serialized.data,status=status.HTTP_200_OK, )
        except Department.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)