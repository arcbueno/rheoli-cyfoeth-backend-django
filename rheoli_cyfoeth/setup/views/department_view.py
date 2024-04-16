from rest_framework import viewsets

from setup.models.department import Department
from setup.serializer import DepartmentSerializer

class DepartmentView(viewsets.ModelViewSet):
    
    queryset = Department.objects.all();
    serializer_class = DepartmentSerializer
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]