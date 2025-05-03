from django.template.context_processors import request
from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Likes

class LikeSerializer(ModelSerializer):

    model=Likes
    fields='__all__'
    read_only_fields=('user','post',)


