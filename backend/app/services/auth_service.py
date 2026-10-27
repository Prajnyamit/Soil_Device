from app.serializers.auth_serializer import LoginSerializer,UserDataSerializer,RegisterSerializer
from app.models.users import User
from app.utils.jwt import (
    generate_access_token,
    generate_refresh_token,
)

class AuthService :
    @staticmethod
    def register(data):
        serializer=RegisterSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return True,serializer.data
        return False ,serializer.errors
    
    @staticmethod
    def userdata(data):
        serializer=UserDataSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return True,serializer.data 
        return False ,serializer.errors
    
    @staticmethod
    def login(data):

        serializer = LoginSerializer(data=data)

        if not serializer.is_valid():
            return False, serializer.errors

        email = serializer.validated_data["email"]
        password = serializer.validated_data["password"]

        try:
            user = User.objects.get(email=email)

        except User.DoesNotExist:
            return False, {
                "message": "Invalid email or password"
            }

        if not user.check_password(password):
            return False, {
                "message": "Invalid email or password"
            }

        access = generate_access_token(user)
        refresh = generate_refresh_token(user)

        return True, {
            "user": {
                "id": user.id,
                "name": user.name,
                "email": user.email,
            },
            "access": access,
            "refresh": refresh,
        }
        
    @staticmethod
    def profile(user):
        return user
