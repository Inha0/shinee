from django.db import models
from django.contrib.auth.models import AbstractUser #인증관련 장고 유저 테이블

# Create your models here.
class User(AbstractUser):
    comment = models.TextField()
    nickname = models.CharField(max_length=30)
    pic = models.ImageField(upload_to="usr/%y")
    def getpic(self):
        if self.pic:
            return self.pic.url
        return "/MEDIA/noimg.png"