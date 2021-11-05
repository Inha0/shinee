from django.db import models
from main.models import User

# Create your models here.
class Album(models.Model):
    album_name= models.CharField(max_length=100)
    album_subname= models.CharField(max_length=100, blank=True)
    album_artist= models.CharField(max_length=100)
    album_img = models.ImageField(upload_to="album_cover/upload")
    release_date = models.DateField()
    artist_no = models.IntegerField(default=0)
    up = models.ManyToManyField(User, blank=True)
    def getimg(self):
        if self.album_img:
            return self.album_img.url
        return "/MEDIA/noimg.png"
    
    def __str__(self):
        return self.album_name