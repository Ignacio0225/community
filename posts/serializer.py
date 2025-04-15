from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Post
from users.serializer import UsernameSerializer



class PostSerializer(ModelSerializer):
    # 이렇게 하면 user를 pk 형식으로 가져옴
    # poster=PrimaryKeyRelatedField(queryset=User.objects.all(),read_only=True)
    replies_count=SerializerMethodField(read_only=True)
    poster=UsernameSerializer(read_only=True)

    class Meta:
        model=Post
        fields="__all__"

    def get_replies_count(self,obj):
        return obj.replies.count()