from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from taggit.models import Tag
from django.template.defaultfilters import date

from .models import Article, Image

class Index(ListView):
    model = Article
    template_name = 'moderate/index.html'
    context_object_name = 'articles'
    paginate_by = 5

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        qs = qs.order_by('-date')
        return qs

    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs)
        context['common_tags'] = Article.tags.most_common()[:8]
        # context['format_date'] = date(Article.date, )

        return context

class ArticleView(DetailView):
    model = Article
    template_name = 'moderate/article.html'
    context_object_name = 'article'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['images'] = Image.objects.filter(article=self.object)
        return context
 

class TagView(ListView):
    model = Article
    template_name = 'moderate/tag.html'
    context_object_name = 'articles'
    paginate_by = 5    
    
    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        tag = Tag.objects.get(pk=self.kwargs['pk'])
        qs = qs.filter(tags=tag).order_by('-date')
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tag'] = Tag.objects.get(pk=self.kwargs['pk'])
        return context

class TagsView(ListView):
    model = Tag
    template_name = 'moderate/tags.html'
    context_object_name = 'tags'
    paginate_by = 5

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        qs = qs.order_by('-id')
        return qs
    
