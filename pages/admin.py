from django.contrib import admin

# Register your models here.

from .models import Diary
class DiaryAdmin(admin.ModelAdmin):
    admin.site.register(Diary)