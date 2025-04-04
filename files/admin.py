from django.contrib import admin
from .models import File
# Register your models here.

@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display = (
        'file',
        'post',
        'updated_at',
    )

    def file_extension(self,obj):
        return obj.get_file_extension() # get_file_extension 메서드를 사용하여 확장자 반환
    file_extension.admin_order_field='file' #정렬 필드 설정
    file_extension.short_description='File Extension' #필드 이름 설정

    list_filter = (
        'post',
        'file_extension',
    )

    search_fields = (
        'file'
    )

    # 확장자 기반으로 겁색하고 싶다면 만들어둘 메서드
    def search_file_extension(queryset,name,value):
        return queryset.filter(file_icontains=value) # 확장자를 포함한 URL 검색