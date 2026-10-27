from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from app.services.auth_service import AuthService
from app.utils.response import success_Message,error_response

class RegisterApiView(APIView):
    authentication_classes=[]
    permission_classes=[]

    def post(self,request):
        success,data=AuthService.register(request.data)
        if success:
            return success_Message(
                message="User Created successfully",
                data=data,
            )
        return error_response(
            message="varification faild",
            data=data,
        )
class LoginApiView(APIView):
    authentication_classes=[]
    permission_classes=[]

    def post(self,request):
        success ,data=AuthService.login(request.data)

        if success:
            return success_Message(
                message="login successful",
                data=data
            )
        
        return error_response(
            message="login failed",
            errors=data
        )


class ProfileAPIView(APIView):
    permission_classes=[IsAuthenticated]

    def get(self,request):
        data=request.user

        if data:
            return success_Message(
                message="profile fetched successfully",
                data=data

            )