from django.contrib import admin
from .models import Post, Image, Comment
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('pk', 'content', 'user')
class ImageAdmin(admin.ModelAdmin):
    list_display = ('pk', 'file', 'post')
class CommentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'content', 'post', 'user')

admin.site.register(Post, PostAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(Comment, CommentAdmin)