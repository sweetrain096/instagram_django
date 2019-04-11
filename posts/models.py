from django.db import models
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    content = models.TextField()
    
    def __str__(self):
        return f'Post : {self.pk} - {self.content}'
    
    def get_absolute_url(self):
        return reverse('posts:detail', args=[self.pk])
        # reverse : object가 가야하는데 뒤의 내용을 실제 path로 만드는 역할.