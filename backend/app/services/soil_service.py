from app.serializers.soil_serializer import SoilSampleSerializer

class SoilService:
    @staticmethod
    def create(user,data):
        serializer=SoilSampleSerializer(data=data)
        if serializer.is_valid():
            serializer.save(user=user)

            return True,serializer.data
        return False,serializer.errors
