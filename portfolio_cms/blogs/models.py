from django.db import models
from django.utils.text import slugify

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    cover_image = models.ImageField(upload_to='blog/')
    markdown_body = models.TextField(help_text="Write content in Markdown")
    tags = models.CharField(max_length=200, help_text="Comma separated tags")
    published_date = models.DateField()
    link = models.URLField(blank=True, null=True, help_text="External link to the full article")
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-published_date']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
