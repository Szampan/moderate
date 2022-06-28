from django.test import TestCase, Client
from django.urls import reverse
from moderate.models import Article, Note
from users.models import Author
from taggit.models import Tag
import json

from django.test.client import RequestFactory

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.author = Author.objects.create(username='test_author')
        self.note_author = Author.objects.create(username='test_note_author', password='test_password')
        self.tag = Tag.objects.create(name='Test tag') 
        self.article = Article.objects.create(
            title='Test article',
            text='Test text',
            author=self.author,
            )
        self.index_url = reverse('moderate:index')
        self.tags_url = reverse('moderate:tags')
        self.tag_url = reverse('moderate:tag', args=[self.tag.pk])
        self.article_url = reverse('moderate:article', args=[self.article.id])
        self.add_note_url = reverse('moderate:add_note', args=[self.article.id])

    def test_index_view(self):
        response = self.client.get(self.index_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'moderate/index.html')

    def test_article_view(self):
        response = self.client.get(self.article_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'moderate/article.html')

    def test_tag_view(self):
        response = self.client.get(self.tag_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'moderate/tag.html')

    def test_tags_view(self):
        response = self.client.get(self.tags_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'moderate/tags.html')

    def test_add_note_view_GET(self):
        article = self.article
        response = self.client.get(self.add_note_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'moderate/add_note.html')
        self.assertEqual(Note.objects.count(), 0)

    def test_add_note_view_POST(self):
        self.client.force_login(self.note_author)
        response = self.client.post(self.add_note_url, {'text': 'Test note'}, follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'moderate/article.html')
        self.assertEqual(Note.objects.count(), 1)




    


