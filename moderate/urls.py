from django.urls import path

from . import views

app_name = 'moderate'
urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('article/<int:pk>/', views.ArticleView.as_view(), name='article'),
    path('tag/<int:pk>/', views.TagView.as_view(), name='tag'),
]