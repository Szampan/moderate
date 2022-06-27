from django.contrib.auth.models import AbstractUser
from django.db import models

class Author(AbstractUser):
    is_staff = models.BooleanField(default=True)
    # is_superuser = models.BooleanField(default=True)
    

    def __str__(self):
        return self.username
