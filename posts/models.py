from django.conf import settings
from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

# Create your models here.
class Post(models.Model):
    content = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # users = models.ManyToManyField(settings.AUTH_USER_MODEL)
    # 윗줄과 같이 작성을 하면
    # user.post_set.all() - 게시글? 좋아요 한 글? 확인할 수 없다.
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='like_posts')
    # image = models.ImageField()
    
    @property
    def like_count(self):
        return self.like_users.count()
        
    def __str__(self):
        return f'Post : {self.pk} - {self.content}'
    
    def get_absolute_url(self):
        return reverse('posts:detail', args=[self.pk])
        # reverse : object가 가야하는데 뒤의 내용을 실제 path로 만드는 역할.
        
class Image(models.Model):
    file = models.ImageField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    
class Comment(models.Model):
    content = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)