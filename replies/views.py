from gc import get_objects

from django.shortcuts import render
from django.template.context_processors import request
from rest_framework.exceptions import NotFound, PermissionDenied
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_204_NO_CONTENT

from .models import Replies
from posts.models import Post
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializer import ReplySerializer
# Create your views here.


class Replies(APIView):

    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self,request,pk):
        try:
            page = request.query_params.get('page',1)
            page = int(page)
        except ValueError:
            page = 1
        page_size = 5
        start = (page-1) * page_size
        end = start + page_size
        post_pk = Post.objects.get(pk=pk)
        all_replies = post_pk.replies.all().order_by('-id')
        serializer = ReplySerializer(all_replies[start:end],many=True)
        return Response(serializer.data)

    def post(self,request,pk):
        serializer = ReplySerializer(data=request.data)
        if serializer.is_valid():
            try:
                post=Post.objects.get(pk=pk)
            except Post.DoesNotExist:
                return Response({"error":"Post Not Found"},status=HTTP_400_BAD_REQUEST)
            reply=serializer.save(
                user=request.user,
                post=post
            )
            serializer=ReplySerializer(reply)
            return Response(serializer.data)
        return Response(serializer.errors,status=HTTP_400_BAD_REQUEST)

class Reply(APIView):
    # pk에 따라 Post를 받아오는 메서드 작성
    def get_post(self,pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise NotFound("게시글이 없습니다")
    # 그 post(Post.object.get(pk=#)) 안에 있는 pk = replies_pk로 수정할 리플을 가져옴
    def get_reply(self,post,replies_pk):
        try:
            return post.replies.get(pk=replies_pk)
        except Replies.DoesNotExist:
            raise NotFound("댓글이 없습니다")

    # get_post에 서 찾아줄 Post를 여기서 설정
    # post 에있는 replies를 replies_pk로 찾아서 reply에 변수 설정
    def put(self,request,pk,replies_pk):
        post=self.get_post(pk=pk)
        # 여기 에있는 post 변수가 get_reply의 post 인수로 들어감
        reply=self.get_reply(post=post,replies_pk=replies_pk)
        if reply.user != request.user:
            raise PermissionDenied("권한 없음")
        serializer=ReplySerializer(
            reply,
            data=request.data,
            partial=True,
        )
        if serializer.is_valid():
            serializer.save(
                post=post,
                user=request.user,
            )
            return Response(serializer.data)
        return Response(serializer.errors,status=HTTP_400_BAD_REQUEST)



    def delete(self,request,pk,replies_pk):
        post=self.get_post(pk=pk)
        reply=self.get_reply(post=post,replies_pk=replies_pk)
        if reply.user != request.user:
            raise PermissionDenied("권한 없음")
        reply.delete()
        return Response(status=HTTP_204_NO_CONTENT)


