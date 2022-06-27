from django.contrib import admin


from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import AuthorCreationForm #, AuthorChangeForm
from .models import Author

class AuthorAdmin(UserAdmin):
    add_form = AuthorCreationForm
    # form = CustomUserChangeForm
    model = Author
    list_display = ('username', 'is_staff')
 
    # def has_add_permission(self, request):
    #     return True

    # def has_delete_permission(self, request, obj=None):
    #     return True

    # def has_change_permission(self, request, obj=None):
    #     return True
    
    # def has_view_permission(self, request, obj=None):
    #     return True


admin.site.register(Author, AuthorAdmin)
