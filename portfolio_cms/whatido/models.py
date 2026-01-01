from django.db import models

class Service(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    icon = models.FileField(upload_to='icons/', help_text="Upload SVG or distinct icon image")

    def __str__(self):
        return self.title
