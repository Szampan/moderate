from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'moderate'
urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('article/<int:pk>/', views.ArticleView.as_view(), name='article'),
    path('article/<int:pk>/add_form', views.AddNote.as_view(), name='add_note'),
    path('tag/<int:pk>/', views.TagView.as_view(), name='tag'),
    path('tags/', views.TagsView.as_view(), name='tags'),
]

if settings.DEBUG:       
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)