from typing import Any
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from setup.controllers.user_controller import UserController
from setup.serializer import GetUserSerializer, UserSerializer, CreateUserSerializer
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.request import Request
from setup.utils.response_utils import ResponseUtils
from setup.utils.validation_utils import ValidationUtils
from returns.result import Result, Success, Failure
from ..utils.models_utils.custom_exception import CustomException
from returns.pipeline import is_successful

class UserView(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users has access to delete and get all users.
    """
         
    def __init__(self, **kwargs: Any):
        self.controller = UserController()
        
    def get_by_id(self, id: int, request: Request) -> Response:
        
        result = self.controller.get_by_id(id=id, token=request.auth.key)
        
        if(not is_successful(result)):
            exception = result.failure()
            return Response(data=exception.message ,status=exception.status_code, exception=True)

        user = result.unwrap()
        return Response(GetUserSerializer(user).data, status=status.HTTP_200_OK)
            
    def get_by_username(self, username: str, request: Request) -> Response:
        
        result = self.controller.get_by_username(username=username, token=request.auth.key)
        
        if(not is_successful(result)):
            exception = result.failure()
            return Response(data=exception.message ,status=exception.status_code, exception=True)

        user = result.unwrap()
        return Response(GetUserSerializer(user).data, status=status.HTTP_200_OK)

    def get(self, request: Request, pk=None) -> Response:
        """
        Return a list of all users.
        """
        
        if(pk != None and type(pk) == int):
            return self.get_by_id(pk, request=request)
        
        if(pk != None and type(pk) == str):
            return self.get_by_username(pk, request=request)
        
        result = self.controller.get_all(request.auth.key)
        if(not is_successful(result)):
            exception = result.failure()
            return Response(status=exception.status_code, data=exception.message, exception=True)
              
        users = [GetUserSerializer(user).data for user in result.unwrap()]
        return Response(users)
    
    def post(self, request: Request, format=None) -> Response:
        """
        Create a new user
        """
        serialized = CreateUserSerializer(data=request.data)
        if serialized.is_valid():
            result = self.controller.create_user(serialized.data)
            if(not is_successful(result)):
                exception = result.failure()
                return Response(status=exception.status_code, data=exception.message, exception=True)
            return Response(result.unwrap(), status=status.HTTP_201_CREATED)
        
        return Response(serialized._errors, status=status.HTTP_400_BAD_REQUEST)
        
    def put(self, request: Request, pk=None,format=None):
        """
        Update a user
        """
        if(pk is None or type(pk) is not int):
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        result: CustomException | None = ValidationUtils.user_is_admin(request=request)
        if(result is not None): 
            return Response(status=result.status_code, data=result.message, exception=True)

        user: User = User.objects.get(id=pk)
        serialized = UserSerializer(user, data=request.data)
        
        if serialized.is_valid():            
            serialized.save()
            return Response(serialized.data, status=status.HTTP_201_CREATED)
    
        return Response(serialized._errors, status=status.HTTP_400_BAD_REQUEST)
        
    
    def delete(self, request: Request, pk=None) -> Response:
        """
        Delete a user
        """    
        if(pk is None or type(pk) != int):
            return Response(status=status.HTTP_400_BAD_REQUEST, data={'detail': 'User Id not found'})
        
        result: Result[int, CustomException] = self.controller.delete_user(pk, token=request.auth.token)
        if(not is_successful(result)):
            exception = result.failure()
            return Response(status=exception.status_code, data=exception.message, exception=True)
        return Response(status=result.unwrap())
    