from rest_framework.authtoken.models import Token
from rest_framework.request import Request
from setup.utils.models_utils.custom_exception import CustomException
from setup.utils.response_utils import ResponseUtils
from rest_framework.response import Response
from django.contrib.auth.models import User


class ValidationUtils:
     def user_is_admin(token) -> CustomException | None:
        """
        Veriry if user has admin permissions.
        """
        try:
            user: User = ResponseUtils.get_user_by_token(key=token)
            if((not user.is_staff)):
                return ResponseUtils.unauthorized_error_data()
            return None
        except Token.DoesNotExist:
            return ResponseUtils.unauthorized_error_data()
                