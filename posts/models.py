from django.db import models
from django.db.models import CharField, TextField, ForeignKey

from common.models import CommonModel
# Create your models here.

class Post(CommonModel):
    subject=CharField(max_length=50)
    poster=ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="posts",
    )
    description=TextField(max_length=3000)
    #category 추가 예정
    #file 추가 예정
    def __str__(self):
        return self.subject