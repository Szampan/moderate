from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Permission
from .models import Author


class AuthorCreationForm(UserCreationForm):
    
    def save(self, commit=True):
        permission_list = [
            'view_article', 'add_article', 'change_article', 'delete_article',
            'view_image', 'add_image', 'change_image', 'delete_image',
            'view_video', 'add_video', 'change_video', 'delete_video',
            ]
        permission_list = list(map(lambda x : Permission.objects.get(codename=x), permission_list))
        user = super().save(commit=False)
        user.save()
        user.user_permissions.add(*permission_list)
        return user

    class Meta:
        model = Author
        fields = ("username", "first_name", "last_name")
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
        }   

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'

