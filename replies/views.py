from django.shortcuts import render
from django.template.context_processors import request
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST

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
