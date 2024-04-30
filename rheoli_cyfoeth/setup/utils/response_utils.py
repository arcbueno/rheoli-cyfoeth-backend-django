
from typing import Tuple, Dict
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .models_utils.custom_exception import CustomException

class ResponseUtils:
    """
    Utility class for creating responses.
    """
    
    
    def unauthorized_error_data() -> CustomException:
       return CustomException(status_code=status.HTTP_401_UNAUTHORIZED, message={'detail': 'Your user has no access to this'})
    
    def not_found_error_data(name : str = 'User') -> CustomException:
       return CustomException(status_code=status.HTTP_404_NOT_FOUND, message={'detail': f'{name} not found'})
    
    def invalid_token_error_data() -> CustomException:
       return CustomException(status_code=status.HTTP_401_UNAUTHORIZED, message={'detail': 'Invalid token'})
    
    def invalid_data_error_data(text: str) -> CustomException:
       return CustomException(status_code=status.HTTP_400_BAD_REQUEST, message={'detail': text})
   
    def get_user_by_token(key) -> User:
         return Token.objects.get(key=key).user