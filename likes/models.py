from django.db import models
from django.db.models import ForeignKey
from rest_framework.fields import BooleanField

from common.models import CommonModel
# Create your models here.


class Likes(CommonModel):
    post=ForeignKey(
        "posts.Post",
        on_delete=models.CASCADE,
        related_name="likes"
    )
    user=ForeignKey(
        'users.User',
        on_delete=models.CASCADE,
        related_name='likes',
    )
    # is_liked=BooleanField(
    #     default=False,
    # )

    # 같은 사람이 두번 선택 하지못하게
    # DB에 저장될때 같은 조합이 두번 올 수 없음 post pk=1 , user pk=1은 한번만 저장됨
    class Meta:
        unique_together=('user','post')