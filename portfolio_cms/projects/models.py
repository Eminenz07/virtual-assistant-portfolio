from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    year = models.IntegerField()
    link_live = models.URLField(blank=True, verbose_name="Live Demo Link")
    link_repo = models.URLField(blank=True, verbose_name="Repository Link")
    cover_image = models.ImageField(upload_to='projects/', help_text="Main image for the project card")

    class Meta:
        ordering = ['-year', 'title']

    def __str__(self):
        return self.title

class ProjectImage(models.Model):
    project = models.ForeignKey(Project, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='projects/gallery/')
    caption = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"Image for {self.project.title}"
