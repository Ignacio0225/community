from django.db import models
from django.db.models import ForeignKey, TextField
from rest_framework.fields import CharField

# Create your models here.
from common.models import CommonModel

class Replies(CommonModel):
    user = ForeignKey(
        'users.User',
        on_delete=models.CASCADE,
        related_name='replies',

    )
    post = ForeignKey(
        'posts.Post',
        on_delete=models.CASCADE,
        related_name='replies'
    )
    description = TextField(
        max_length=1000,
    )

    def __str__(self):
        return self.description