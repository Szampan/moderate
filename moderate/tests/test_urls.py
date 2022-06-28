from django.test import SimpleTestCase
from django.urls import reverse, resolve
from moderate.views import Index, ArticleView, TagView, TagsView, AddNote

class TestUrls(SimpleTestCase):

    def test_index_url_resolves(self):
        url = reverse('moderate:index')
        # print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, Index)  

    def test_tags_url_resolves(self):
        url = reverse('moderate:tags')
        self.assertEquals(resolve(url).func.view_class, TagsView)  

    def test_article_url_resolves(self):
        url = reverse('moderate:article', args=[1])
        self.assertEquals(resolve(url).func.view_class, ArticleView)  

    def test_tag_url_resolves(self):
        url = reverse('moderate:tag', args=[1])
        self.assertEquals(resolve(url).func.view_class, TagView)