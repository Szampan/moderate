from django.contrib import admin
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import AuthorCreationForm 
from .models import Author


class AuthorAdmin(UserAdmin):
    add_form = AuthorCreationForm
    model = Author
    list_display = ('username', 'is_staff')
 

admin.site.register(Author, AuthorAdmin)
