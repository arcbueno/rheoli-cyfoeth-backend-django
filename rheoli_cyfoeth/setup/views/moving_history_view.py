from typing import Any
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from setup.controllers.moving_history_controller import MovingHistoryController
from setup.serializer import CreateMovingHistorySerializer, MovingHistorySerializer
from returns.pipeline import is_successful

from rest_framework.views import APIView

   
class MovingHistoryView(APIView):
    
    def __init__(self, **kwargs: Any) -> None:
        self.controller = MovingHistoryController()
        super().__init__(**kwargs)

    def post(self, request: Request, format=None):
        """
        Return a list of all users.
        """
        serialized = CreateMovingHistorySerializer(data=request.data)
        if serialized.is_valid():
            result = self.controller.create(serialized.data)
            if(not is_successful(result)):
                exception = result.failure()
                return Response(data=exception.message, status=exception.status_code)
            
            return Response( status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
        