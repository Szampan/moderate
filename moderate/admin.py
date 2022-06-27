from django.contrib import admin
from embed_video.admin import AdminVideoMixin
from .models import Article, Image, Video, Note

class VideoInline(admin.TabularInline):
    model = Video
    extra = 1 

class ImageInline(admin.TabularInline):
    model = Image
    extra = 1

class ArticleAdmin(admin.ModelAdmin):
    inlines = [VideoInline, ImageInline]

class  VideoAdmin(AdminVideoMixin, admin.ModelAdmin):
	pass

admin.site.register(Article, ArticleAdmin)
admin.site.register(Note)


