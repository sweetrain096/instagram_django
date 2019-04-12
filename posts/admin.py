from django.contrib import admin
from .models import Post, Image
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('pk', 'content', )
class ImageAdmin(admin.ModelAdmin):
    list_display = ('pk', 'file', 'post')

admin.site.register(Post, PostAdmin)
admin.site.register(Image, ImageAdmin)