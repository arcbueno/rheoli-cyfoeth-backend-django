from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from setup.serializer import GetUserSerializer, UserSerializer, CreateUserSerializer
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.request import Request
from setup.utils.response_utils import ResponseUtils
from setup.utils.validation_utils import ValidationUtils

class UserView(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users has access to delete and get all users.
    """
        
    def get_by_id(self, id: int, request: Request) -> Response:
        
        # Non-admin users are allow to only get its user data
        try:
            user: User = ResponseUtils.get_user_by_token(request.auth.key)
            if(user.id != id and (not user.is_staff)):
                return ResponseUtils.return_unauthorized()
        except Token.DoesNotExist:
            return ResponseUtils.return_unauthorized()
        
        try:
            return Response(GetUserSerializer(User.objects.get(id=id)).data)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    def get_by_username(self, username: str, request: Request) -> Response:
        
        # Non-admin users are allow to only get its user data
        try:
            user: User = ResponseUtils.get_user_by_token(request.auth.key)
            if(user.username != username and (not user.is_staff)):
                return ResponseUtils.return_unauthorized()
        except Token.DoesNotExist:
            return ResponseUtils.return_unauthorized()
        
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
        
        result = ValidationUtils.user_is_admin(request=request)
        if(result is not None): 
            return result
              
        users = [GetUserSerializer(user).data for user in User.objects.all()]
        return Response(users)
    
    '''
    Create a new user
    '''
    def post(self, request: Request, format=None) -> Response:
        serialized = CreateUserSerializer(data=request.data)
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
        
        return Response(serialized._errors, status=status.HTTP_400_BAD_REQUEST)
        
    '''
    Update a user
    '''
    def put(self, request: Request, pk=None,format=None):
        result = ValidationUtils.user_is_admin(request=request)
        if(result is not None): 
            return result
        
        if(pk is not None and type(pk) is int):
            user: User = User.objects.get(id=pk)
            serialized = UserSerializer(user, data=request.data)
            
            if serialized.is_valid():            
                serialized.save()
                return Response(serialized.data, status=status.HTTP_201_CREATED)
        
        return Response(serialized._errors, status=status.HTTP_400_BAD_REQUEST)
    
    '''
    Delete a user
    '''    
    def delete(self, request: Request, pk=None) -> Response:
        result = ValidationUtils.user_is_admin(request=request)
        if(result is not None): 
            return result
        if(pk is None or type(pk) != int):
            return Response(status=status.HTTP_400_BAD_REQUEST, data={'details': 'User Id not found'})
        
        user = User.objects.get(id=pk)
        User.delete(user)
        return Response(status=status.HTTP_204_NO_CONTENT)
    