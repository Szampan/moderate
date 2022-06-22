from django.db import models

from .tools import *

# autor - user
# class Author(models.Model):
#     first_name = 
#     second_name = 
#     pass



class Article(models.Model):
    # author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    # content = 

class Image(models.Model):
    article = models.ForeignKey(Article, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=image_upload_handler, blank=True)


class Notes(models.Model):
    # article = 
    # note_author = 
    pass
