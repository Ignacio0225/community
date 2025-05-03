from django.shortcuts import render
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.views import APIView

from likes.models import Likes
from likes.serializer import LikeSerializer
from posts.models import Post


# Create your views here.

class LikeToggle(APIView):
    permission_classes = [IsAuthenticated]

    def get_post(self,pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise NotFound


    def post(self,request,pk):
        post=self.get_post(pk)
        user=request.user

        # 존재 여부만 알기위해서는 exists()를 써야 하지만 이후 조작을 해야하기때문에 first()로 쿼리셋을 받아와야함
        like_obj = Likes.objects.filter(post=post, user=user).first()

        if like_obj:
            # 만약 like_obj가 참이면 삭제 (post, user가 이미있음, 즉 좋아요가 눌린상태)
            like_obj.delete()
            return Response({'message':"좋아요 취소"}, status=HTTP_200_OK)
        else:
            # 아니면 post와 user를 저장
            like = Likes.objects.create(post=post,user=user)
            serializer = LikeSerializer(like)
            return Response(serializer.data,status=HTTP_200_OK)
