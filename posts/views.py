from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_204_NO_CONTENT
from rest_framework.exceptions import NotFound, PermissionDenied
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializer import PostSerializer
from .models import Post

# Create your views here.


class Posts(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self,request):
        try:
            page = request.query_params.get('page',1)
            page = int(page)
        except ValueError:
            page = 1
        page_size = 5
        start = (page-1) * page_size
        end = start + page_size
        # 출력 순서를 역순으로(최신순) .order_by('-created_at')은 업로드순
        all_posts=Post.objects.all().order_by('-id')
        serializer=PostSerializer(all_posts[start:end],many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer=PostSerializer(data=request.data)
        if serializer.is_valid():
            post=serializer.save(
                poster=request.user
            )
            serializer=PostSerializer(post)
            return Response(serializer.data)
        return Response(serializer.errors,status=HTTP_400_BAD_REQUEST)

class PostDetail(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self,pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise NotFound

    def get(self,pk):
        post=self.get_object(pk)
        serializer=PostSerializer(post)
        return Response(serializer.data)

    def put(self,request,pk):
        post=self.get_object(pk)
        if post.poster != request.user:
            raise PermissionDenied
        else:
            serializer = PostSerializer(post, data=request.data, partial=True)
            if serializer.is_valid():
                post = serializer.save()
                serializer = PostSerializer(post)
                return Response(serializer.data)
            else:
                return Response(serializer.errors, HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        post=self.get_object(pk)
        if post.poster != request.user:
            raise PermissionDenied
        else:
            post.delete()
            return Response(status=HTTP_204_NO_CONTENT)

