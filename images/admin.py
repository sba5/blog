from django.contrib import admin
#from .models import Post, Photo
# Register your models here.
from .models import Photo

class PhotoAdmin(admin.ModelAdmin):
    admin.site.register(Photo)

#class PostAdmin(admin.ModelAdmin):
#    inlines = [PhotoInline, ]

#admin.site.register(Post, PostAdmin)

# from .models import Members
# class MembersAdmin(aWdmin.ModelAdmin):
#     admin.site.register(Members)