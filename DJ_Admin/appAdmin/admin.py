from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import UserInfo


@admin.register(UserInfo)
class UserInfoAdmin(ModelAdmin):
    pass