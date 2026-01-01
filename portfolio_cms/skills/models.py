from django.db import models

class Skill(models.Model):
    CATEGORY_CHOICES = [
        ('FE', 'Frontend'),
        ('BE', 'Backend'),
        ('Tools', 'Tools & DevOps'),
        ('Other', 'Other'),
    ]
    name = models.CharField(max_length=100)
    proficiency = models.IntegerField(help_text="Percentage 0-100")
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='Other')
    icon = models.FileField(upload_to='skills/', null=True, blank=True)

    def __str__(self):
        return self.name
