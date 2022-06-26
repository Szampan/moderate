from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager
from embed_video.fields import EmbedVideoField

from .tools import *

# autor - user
# class Author(models.Model):
#     first_name = 
#     second_name = 
#     pass


class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    tags = TaggableManager()

    def get_absolute_url(self):
        return reverse('moderate:article', args=[self.pk])


    def __str__(self):
        return self.title

class Image(models.Model):
    article = models.ForeignKey(Article, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=image_upload_handler) #, blank=True)

    # def __str__(self):
    #     return self.article.title

class Video(models.Model):
    article = models.ForeignKey(Article, default=None, on_delete=models.CASCADE) 
    url = EmbedVideoField(blank=True)
    
    def __str__(self):
        return self.url

class Notes(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE) 
    note_author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    text = models.TextField(max_length=1000)
    

