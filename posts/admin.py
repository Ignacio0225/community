from django.contrib import admin
from .models import Post
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        "subject",
        "poster",
        "created_at",
        "updated_at",

    )

    list_filter = (
        "created_at",
        "updated_at",
    )

    search_fields = (
        "subject",
        "poster__username",
    )
    list_per_page = 20