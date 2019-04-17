from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

from imagekit.models import ProcessedImageField
# field 설정
from imagekit.processors import ResizeToFill
# Create your models here.
class User(AbstractUser):
    followers = models.ManyToManyField(
                    settings.AUTH_USER_MODEL, 
                    related_name='followings')


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=30)
    introduction = models.TextField()
    image = ProcessedImageField(
                    processors=[ResizeToFill(150, 150)],
                    format='JPEG',
                    options={'quality': 100},
                )