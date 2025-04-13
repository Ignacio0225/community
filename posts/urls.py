from django.urls import path
from posts.views import Posts, PostDetail
from replies.views import Replies

urlpatterns=[
    path('',Posts.as_view(), name='post-list'),
    path('<int:pk>/',PostDetail.as_view(), name='post-detail'),
    path('<int:pk>/replies',Replies.as_view(), name='post-replies'),
]