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
    # Use timezone.now or datetime.date.today
    testimonial_date = models.DateField(blank=True, null=True, help_text="Date of testimonial")

    def save(self, *args, **kwargs):
        import random
        
        # Default avatar lists
        male_avatars = ['avatar-1.png', 'avatar-4.png']
        female_avatars = ['avatar-2.png', 'avatar-3.png']
        all_defaults = male_avatars + female_avatars
        
        # Logic to assign/update avatar
        should_assign_new = False
        
        if not self.client_image:
            should_assign_new = True
        else:
            # Check if current image is a default avatar
            current_filename = self.client_image.split('/')[-1]
            if current_filename in all_defaults:
                # If gender mismatch, re-assign
                if self.gender == 'Male' and current_filename in female_avatars:
                    should_assign_new = True
                elif self.gender == 'Female' and current_filename in male_avatars:
                    should_assign_new = True

        if should_assign_new:
            if self.gender == 'Male':
                avatar = random.choice(male_avatars)
            else:
                avatar = random.choice(female_avatars)
            self.client_image = f"./assets/images/{avatar}"
            
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.client_name} - {self.designation}"
