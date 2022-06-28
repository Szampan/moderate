from django.test import TestCase
from users.forms import AuthorCreationForm
from users.models import Author


class TestForms(TestCase):

    def test_author_creation_form_valid(self):
        form = AuthorCreationForm(data={
            'username': 'test_username',
            'first_name': 'test',
            'last_name': 'test',
            'password1': 'unique123',
            'password2': 'unique123',
        })
        self.assertTrue(form.is_valid())

    def test_author_creation_form_wrong_password(self):
        form = AuthorCreationForm(data={
            'username': 'test_username',
            'first_name': 'test',
            'last_name': 'test',
            'password1': 'password',
            'password2': 'password',
        })
        self.assertFalse(form.is_valid())

    def test_author_creation_form_save_permissions(self):
        permission_list = [
            'view_article', 'add_article', 'change_article', 'delete_article',
            'view_image', 'add_image', 'change_image', 'delete_image',
            'view_video', 'add_video', 'change_video', 'delete_video',
            ]
        form = AuthorCreationForm(data={
            'username': 'test_username',
            'password1': 'unique123',
            'password2': 'unique123',
        })
        form.save()
        created_author = Author.objects.get(username='test_username')
        author_permissions = created_author.user_permissions.all().values_list('codename', flat=True)
        self.assertEqual(set(author_permissions), set(permission_list))