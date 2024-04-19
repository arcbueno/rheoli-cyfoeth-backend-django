
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class ResponseUtils:
    """
    Utility class for creating responses.
    """
    def return_unauthorized(self):
       return  Response(exception=True, status=status.HTTP_401_UNAUTHORIZED, data={'detail': 'Your user has no access to this'})
   
    def get_user_by_token(self, key) -> User:
         return Token.objects.get(key=key).user