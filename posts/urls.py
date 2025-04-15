from django.urls import path
from posts.views import Posts, PostDetail
from replies.views import Replies,Reply

urlpatterns=[
    path('',Posts.as_view(), name='post-list'),
    path('<int:pk>/',PostDetail.as_view(), name='post-detail'),
    path('<int:pk>/replies/',Replies.as_view(), name='post-replies'),
    path('<int:pk>/replies/<int:replies_pk>/',Reply.as_view(), name='replies-detail'),
]