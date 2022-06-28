from django.test import TestCase
from moderate.models import Article
from users.models import Author


class TestModels(TestCase):

    def setUp(self):
        self.author = Author.objects.create(username='test_author')
        self.article = Article.objects.create(
            title='Test article',
            text='Test text',
            author=self.author,
            )
  

    def test_article_absolute_url(self):
        self.assertEqual(self.article.get_absolute_url(), '/article/{}/'.format(self.article.id))
