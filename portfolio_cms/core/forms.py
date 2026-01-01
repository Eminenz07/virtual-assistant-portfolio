from django import forms
from whatido.models import Service
from testimonials.models import Testimonial
from experience.models import Experience
from skills.models import Skill
from certifications.models import Certification
from projects.models import Project, ProjectImage
from blogs.models import BlogPost

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = '__all__'

class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ['client_name', 'designation', 'testimonial_text', 'gender']

class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = '__all__'
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }

class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = '__all__'

class CertificationForm(forms.ModelForm):
    class Meta:
        model = Certification
        fields = '__all__'
        widgets = {
            'date_earned': forms.DateInput(attrs={'type': 'date'}),
        }

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = '__all__'
        exclude = ('slug', 'created_at', 'author') # Exclude auto/read-only fields
        widgets = {
            'published_date': forms.DateInput(attrs={'type': 'date'}),
        }
