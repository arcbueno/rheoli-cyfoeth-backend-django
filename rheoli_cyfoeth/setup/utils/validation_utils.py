from rest_framework.authtoken.models import Token
from rest_framework.request import Request
from setup.utils.response_utils import ResponseUtils
from rest_framework.response import Response
from django.contrib.auth.models import User


class ValidationUtils:
     def user_is_admin(request: Request) -> Response | None:
        """
        Veriry if user has admin permissions.
        """
        try:
            user: User = ResponseUtils.get_user_by_token(key=request.auth.key)
            if((not user.is_staff)):
                return ResponseUtils.return_unauthorized()
            return None
        except Token.DoesNotExist:
            return ResponseUtils.return_unauthorized()
                