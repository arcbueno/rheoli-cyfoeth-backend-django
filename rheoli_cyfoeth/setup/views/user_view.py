from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from setup.serializer import GetUserSerializer, UserSerializer
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.request import Request
from setup.utils.response_utils import ResponseUtils

class UserView(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    # permission_classes = [permissions.IsAdminUser]
        
    def get_by_id(self, id: int, request: Request) -> Response:
        
        # Non-admin users are allow to only get its user data
        try:
            user: User = ResponseUtils().get_user_by_token(request.auth.key)
            if(user.id != id and (not user.is_staff)):
                return ResponseUtils().return_unauthorized()
        except Token.DoesNotExist:
            return ResponseUtils().return_unauthorized()
        
        try:
            return Response(GetUserSerializer(User.objects.get(id=id)).data)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    def get_by_username(self, username: str, request: Request) -> Response:
        
        # Non-admin users are allow to only get its user data
        try:
            user: User = ResponseUtils().get_user_by_token(request.auth.key)
            if(user.username != username and (not user.is_staff)):
                return ResponseUtils().return_unauthorized()
        except Token.DoesNotExist:
            return ResponseUtils().return_unauthorized()
        
        try:
            return Response(GetUserSerializer(User.objects.get(username=username)).data)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    '''
    Return a list of all users or just one by id.
    '''	
    def get(self, request: Request, pk=None) -> Response:
        """
        Return a list of all users.
        """
        
        if(pk != None and pk is int):
            return self.get_by_id(pk, request=request)
        
        if(pk != None and type(pk) == str):
            return self.get_by_username(pk, request=request)
        
        try:
            user: User = Token.objects.get(key=request.auth.key).user
            if(not user.is_staff):
                return ResponseUtils().return_unauthorized()
        except Token.DoesNotExist:
            return ResponseUtils().return_unauthorized()
              
        users = [GetUserSerializer(user).data for user in User.objects.all()]
        return Response(users)
    
    '''
    Create a new user
    '''
    def post(self, request, format=None) -> Response:
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
        
    def delete(self, request, pk=None) -> Response:
        try:
            user: User = Token.objects.get(key=request.auth.key).user
            if(not user.is_staff):
                return ResponseUtils().return_unauthorized()
        except Token.DoesNotExist:
            return ResponseUtils().return_unauthorized()
        
        if(pk is None or type(pk) != int):
            return Response(status=status.HTTP_400_BAD_REQUEST, data={'details': 'User Id not found'})
        
        user = User.objects.get(id=pk)
        User.delete(user)
        return Response(status=status.HTTP_204_NO_CONTENT)
            
        
            