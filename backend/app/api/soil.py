from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from app.services.soil_service import SoilService
from app.utils.response import success_Message,error_response


class SoilSampleApiView(APIView):
    permission_classes=[IsAuthenticated]

    def post(self,request):
        success,data=SoilService.create(request.user,request.data)

        if success:
            return success_Message(
                message="Soil sample saved",
                data=data
            )
    
        return error_response(
            message="soil data validation failed",
            errors=data
        )