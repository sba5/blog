from django.contrib import admin

# Register your models here.

from .models import Members
class MembersAdmin(admin.ModelAdmin):
    admin.site.register(Members)
#, MembersAdmin