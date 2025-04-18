from rest_framework.serializers import ModelSerializer
from .models import Replies
from users.serializer import UsernameSerializer



class ReplySerializer(ModelSerializer):
    user = UsernameSerializer(read_only=True)


    class Meta:
        model=Replies
        fields='__all__'

