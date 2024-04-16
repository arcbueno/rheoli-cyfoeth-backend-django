from rest_framework import viewsets

from setup.models.employee import Employee
from setup.serializer import EmployeeSerializer

class EmployeeView(viewsets.ModelViewSet):
    
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]