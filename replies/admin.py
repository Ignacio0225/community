from django.contrib import admin
from .models import Replies

# Register your models here.

@admin.register(Replies)
class ReplyAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'post',
        'description',
    )