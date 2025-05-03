from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    class GenderChoices(models.TextChoices):
        MALE = ('male','Male')
        FEMALE = ('female','Female')
    class LanguageChoices(models.TextChoices):
        KR = ('kr', 'Korean')
        EN = ('en', 'English')
        ES = ('es', 'Español')
    first_name = models.CharField(
        max_length=150,
        editable=False,
    )
    last_name = models.CharField(
        max_length=150,
        editable=False,
    )
    avatar = models.URLField(
        blank=True,
    )
    # nickname개념, username(일반적인 로그인 ID)와 다름
    # 동일한 이름을 갖지 못하게 유니크 옵션 추가
    name = models.CharField(
        max_length=150,
        default="",
        unique=True
    )
    is_host = models.BooleanField(
        default=False,
    )
    gender = models.CharField(
        max_length=10,
        choices=GenderChoices.choices,
    )
    language = models.CharField(
        max_length=2,
        choices=LanguageChoices.choices,
    )
