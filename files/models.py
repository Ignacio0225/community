from tkinter.constants import CASCADE
from django.db.models import ForeignKey
from rest_framework.fields import URLField
import os

from common.models import CommonModel
# Create your models here.


class File(CommonModel):
    file=URLField()
    post=ForeignKey(
        'posts.Post',
        on_delete=CASCADE,
        null=True,
        blank=True,
        related_name='files',
    )
    def __str__(self):
        return f'File for {self.post.subject}'

    #파일 확장자를 추출하는 메서드
    def get_file_extension(self):
        return os.path.splitext(self.file.path)[-1].lower()#확장자 추출(소문자)