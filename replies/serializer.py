from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField
from .models import Replies
from users.serializer import UsernameSerializer



class ReplySerializer(ModelSerializer):
    # user=request.user를 했어도 프론트에서 는 read_only인지 모르기때문에 read_only로 설정 해줘야함
    # 이 시리얼라이저는 username을 이름(string)으로 가져오기 위함.
    user = UsernameSerializer(read_only=True)
    # 백엔드에서 view에 post=post 를 작성 해줬지만 프론트에서는 read_only로 있어야 작성하지 않아도
    # 백엔드에서 설정한 post=post로 자동 저장, 그리고 post는 pk(숫자)로 받아오기때문에 PrimaryKeyRelatedField 사용해줌
    post = PrimaryKeyRelatedField(read_only=True)


    class Meta:
        model=Replies
        fields='__all__'

