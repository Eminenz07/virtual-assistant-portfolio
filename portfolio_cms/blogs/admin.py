from django.contrib import admin
from .models import BlogPost

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_date', 'is_published')
    list_filter = ('is_published', 'published_date', 'tags')
    search_fields = ('title', 'markdown_body')
    prepopulated_fields = {'slug': ('title',)}
