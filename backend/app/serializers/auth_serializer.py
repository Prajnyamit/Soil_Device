from app.models.users import User
from rest_framework import serializers

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        min_length=8
    )
    class Meta:
        model = User
        fields = [
            "name",
            "email",
            "password"
        ]
    def create(self, validated_data):
        password=validated_data.pop("password")
        user=User(**validated_data)
        user.set_password(password)
        user.save()
        return user

class UserDataSerializer(serializers.Serializer):
    class Meta:
        model=User
        fields=[
            "first_name",
            "last_name",
        ]
        def create(self,validated_data):
            User.first_name=validated_data["first_name"]
            User.last_name=validated_data["last_name"]

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)