from typing import List
from returns.result import Result, Success, Failure
from ..utils.models_utils.custom_exception import CustomException
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.request import Request
from setup.utils.response_utils import ResponseUtils
from setup.utils.validation_utils import ValidationUtils
from rest_framework.serializers import ReturnDict

class UserController:
    
    def get_by_id(self, id, token) -> Result[User, CustomException]:
        try:
            # Non-admin users are allowed to only get its user data
            user: User = ResponseUtils.get_user_by_token(token)
            if(user.id != id and (not user.is_staff)):
                return Failure(ResponseUtils.unauthorized_error_data())
        except Token.DoesNotExist:
            return Failure(ResponseUtils.invalid_token_error_data())
        
        try:
            return Success(User.objects.get(id=id))
        except User.DoesNotExist:
            return Failure(ResponseUtils.not_found_error_data())
        
    def get_by_username(self, username, token) -> Result[User, CustomException]:
        try:
            # Non-admin users are allowed to only get its user data
            user: User = ResponseUtils.get_user_by_token(token)
            if(user.username != username and (not user.is_staff)):
                exception_data = ResponseUtils.unauthorized_error_data()
                return Failure(exception_data)
        except Token.DoesNotExist:
            return Failure(ResponseUtils.invalid_token_error_data())
        
        try:
            return Success(User.objects.get(username=username))
        except User.DoesNotExist:
            return Failure(ResponseUtils.not_found_error_data())
        
    def get_all(self, token) -> Result[List[User], CustomException]:
        result = ValidationUtils.user_is_admin(token)
        if(result is not None): 
            return Failure(result)
        return Success(User.objects.all())
    
    def create_user(self, user_data: ReturnDict) -> Result[User, CustomException]: 
            try:
                user = User.objects.create_user(
                    user_data['username'],
                    user_data['email'],
                    user_data['password'],
                    first_name=user_data['first_name'],
                    last_name=user_data['last_name'],
                    is_staff=user_data['is_staff']
                )
                return Success(user)
            except Exception as e:
                return Failure(CustomException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, message={'detail': str(e)}))
            
    def delete_user(self, id: int, token) -> Result[int, CustomException]:
        try:
            result = ValidationUtils.user_is_admin(token)
            if(result is not None): 
                return result
            user = User.objects.get(id=id)
            user.delete()
            return Success(status.HTTP_204_NO_CONTENT)
        except User.DoesNotExist:
            return Success(status.HTTP_204_NO_CONTENT)
        
            