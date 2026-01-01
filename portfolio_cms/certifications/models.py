from django.db import models

class Certification(models.Model):
    title = models.CharField(max_length=200)
    issuer = models.CharField(max_length=200)
    date_earned = models.DateField()
    credential_url = models.URLField(blank=True)
    certificate_image = models.ImageField(upload_to='certifications/', blank=True, null=True)

    class Meta:
        ordering = ['-date_earned']

    def __str__(self):
        return self.title
