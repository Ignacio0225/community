from django.contrib import admin
from likes.models import Likes
# Register your models here.

@admin.register(Likes)
class LikesAdmin(admin.ModelAdmin):
    list_display =(
        "post",
        'user'
    )
    list_per_page = 3