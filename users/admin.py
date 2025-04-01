from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
# Register your models here.

@admin.register(User)
class CustomUserAdmin(UserAdmin):

    fieldsets = (
        ('Profile',
        {'fields':(
                'avatar',
                'username',
                'password',
                'name',
                'email',
                'is_host',
                'gender',
                'language',
                ),
                'classes':(
                        'wide',
                ),
        },
        ),
        # super user가 일반 유저에게 설정 해줄수 있는 기능들
        ('Permission',
        {'fields':(
                'is_active',
                'is_staff',
                'is_superuser',
                'groups',
                'user_permissions',
                ),
                'classes':(
                    'collapse',
                ),
        },
        ),
        ('Important date',
            {'fields':(
                'last_login',
                'date_joined',
            ),
                'classes':(
                    'collapse',
                ),
            },
        ),
    )