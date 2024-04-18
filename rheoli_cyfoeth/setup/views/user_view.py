from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from setup.serializer import GetUserSerializer, UserSerializer
from rest_framework import status, request

class UserView(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    # authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAdminUser]
    
    def get_by_id(self, id: int):
        
        try:
            return Response(GetUserSerializer(User.objects.get(id=id)).data)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk=None):
        """
        Return a list of all users.
        """
        if(pk != None):
            return self.get_by_id(pk)
        users = [GetUserSerializer(user).data for user in User.objects.all()]
        return Response(users)
    
    def post(self, request, format=None):
        serialized = UserSerializer(data=request.data)
        if serialized.is_valid():
            User.objects.create_user(
                serialized.data['username'],
                serialized.data['email'],
                serialized.data['password'],
                first_name=serialized.data['first_name'],
                last_name=serialized.data['last_name'],
                is_staff=serialized.data['is_staff']
            )
            return Response(serialized.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serialized._errors, status=status.HTTP_400_BAD_REQUEST) 
            



# from rest_framework import viewsets

# from setup.models.employee import Employee
# from setup.serializer import EmployeeSerializer

# class EmployeeView(viewsets.ModelViewSet):
    
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer
#     # authentication_classes = [BasicAuthentication]
#     # permission_classes = [IsAuthenticated]