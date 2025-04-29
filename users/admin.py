from django.contrib import admin

from users.models import User


@admin.register(User)
class AdminUser(admin.ModelAdmin):
    list_display = ['email', 'username', 'date_of_birth',
                    'is_active', 'is_staff',
                    'created', 'updated']
    list_filter = ['date_of_birth', 'is_active', 'is_staff']
