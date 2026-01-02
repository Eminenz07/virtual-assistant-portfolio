from django.db import models

class Service(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    ICON_CHOICES = [
        ('create-outline', 'Writing/Content (Pen)'),
        ('code-slash-outline', 'Development (Code)'),
        ('bar-chart-outline', 'Strategy/Analytics (Chart)'),
        ('brush-outline', 'Design (Brush)'),
        ('mic-outline', 'Speaking/Audio (Mic)'),
        ('people-outline', 'Management (People)'),
        ('camera-outline', 'Photography (Camera)'),
        ('videocam-outline', 'Video (Camera)'),
        ('mail-outline', 'Email/Communication (Mail)'),
    ]
    icon_name = models.CharField(max_length=50, choices=ICON_CHOICES, default='create-outline', help_text="Select an icon for this service")

    def __str__(self):
        return self.title
