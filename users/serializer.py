from email.policy import default

from rest_framework.serializers import ModelSerializer, CharField
from .models import User


class SimpleUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = (
            'name',
            'avatar',
            'username',
        )

class DetailUserSerializer(ModelSerializer):
    class Meta:
        model=User
        exclude=(
            'password',
            'gender',
            'language',

        )

class CreateUserSerializer(ModelSerializer):
    password = CharField(
        min_length=8,
        max_length=16,
        write_only=True,
    )
    class Meta:
        model = User
        fields =(
            "username",
            "password",
            "email",
            "name",
        )
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"],
            password=validated_data["password"],
            email=validated_data["email"],
            name=validated_data.get("name","")
        )
        return user

class ChangePasswordSerializer(ModelSerializer):
    old_password = CharField(write_only=True)
    new_password = CharField(write_only=True,min_length=8,max_length=16,)
    class Meta:
        model = User
        fields =(
            'old_password',
            'new_password',
        )