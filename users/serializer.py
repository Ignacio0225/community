from email.policy import default

from rest_framework.serializers import ModelSerializer, CharField
from .models import User

class UsernameSerializer(ModelSerializer):
    class Meta:
        model=User
        fields=(
            'name',
        )

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
        #유저 가입할때 password 를 해싱해주기 위함 (.create_user)
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"],
            password=validated_data["password"],
            email=validated_data["email"],
            name=validated_data.get("name","")
        )
        return user

#이전 비밀번호를 비교 하고 새로운 비밀번호 를 받아 와서 validate 를 하기 위함(view 에서)
class ChangePasswordSerializer(ModelSerializer):
    old_password = CharField(write_only=True)
    new_password = CharField(write_only=True,min_length=8,max_length=16,)
    class Meta:
        model = User
        fields =(
            'old_password',
            'new_password',
        )