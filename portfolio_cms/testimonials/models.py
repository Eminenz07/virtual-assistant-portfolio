from django.db import models

class Testimonial(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]
    client_name = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)
    testimonial_text = models.TextField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default='Male')
    client_image = models.CharField(max_length=255, blank=True, null=True, help_text="Auto-assigned based on gender")

    def save(self, *args, **kwargs):
        import random
        if not self.client_image:
            if self.gender == 'Male':
                avatar = random.choice(['avatar-1.png', 'avatar-4.png'])
            else:
                avatar = random.choice(['avatar-2.png', 'avatar-3.png'])
            self.client_image = f"./assets/images/{avatar}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.client_name} - {self.designation}"
