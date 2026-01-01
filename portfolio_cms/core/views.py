from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import (
    ServiceForm, TestimonialForm, ExperienceForm, SkillForm, 
    CertificationForm, ProjectForm, BlogPostForm
)
from whatido.models import Service
from testimonials.models import Testimonial
from experience.models import Experience
from skills.models import Skill
from certifications.models import Certification
from projects.models import Project
from blogs.models import BlogPost

def root_redirect(request):
    return redirect('dashboard_home')

def dashboard_login(request):
    if request.user.is_authenticated:
        return redirect('dashboard_home')
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard_home')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, 'core/login.html', {'form': form})

def dashboard_logout(request):
    logout(request)
    return redirect('login')

@login_required
def dashboard_home(request):
    counts = {
        'services': Service.objects.count(),
        'testimonials': Testimonial.objects.count(),
        'experience': Experience.objects.count(),
        'projects': Project.objects.count(),
        'blogs': BlogPost.objects.count(),
    }
    return render(request, 'core/dashboard_home.html', {'counts': counts})

# --- Helper for Generic CRUD ---
def handle_crud(request, model_class, form_class, template_list, template_form, redirect_list, pk=None, delete=False):
    instance = get_object_or_404(model_class, pk=pk) if pk else None
    
    if delete:
        if request.method == 'POST':
            instance.delete()
            return redirect(redirect_list)
        return render(request, 'core/confirm_delete.html', {'object': instance, 'redirect_url': redirect_list})

    if request.method == 'POST':
        form = form_class(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            return redirect(redirect_list)
    else:
        form = form_class(instance=instance)
    
    return render(request, template_form, {'form': form, 'title': model_class._meta.verbose_name_plural.title()})

# --- Service CRUD ---
@login_required
def service_list(request):
    items = Service.objects.all()
    return render(request, 'core/service_list.html', {'items': items})

@login_required
def service_create(request):
    return handle_crud(request, Service, ServiceForm, 'core/service_list.html', 'core/service_form.html', 'service_list')

@login_required
def service_edit(request, pk):
    return handle_crud(request, Service, ServiceForm, 'core/service_list.html', 'core/service_form.html', 'service_list', pk=pk)

@login_required
def service_delete(request, pk):
    return handle_crud(request, Service, ServiceForm, None, None, 'service_list', pk=pk, delete=True)

# --- Testimonial CRUD ---
@login_required
def testimonial_list(request):
    items = Testimonial.objects.all()
    return render(request, 'core/testimonial_list.html', {'items': items})

@login_required
def testimonial_create(request):
    return handle_crud(request, Testimonial, TestimonialForm, None, 'core/testimonial_form.html', 'testimonial_list')

@login_required
def testimonial_edit(request, pk):
    return handle_crud(request, Testimonial, TestimonialForm, None, 'core/testimonial_form.html', 'testimonial_list', pk=pk)

@login_required
def testimonial_delete(request, pk):
    return handle_crud(request, Testimonial, TestimonialForm, None, None, 'testimonial_list', pk=pk, delete=True)

# --- Experience CRUD ---
@login_required
def experience_list(request):
    items = Experience.objects.all()
    return render(request, 'core/experience_list.html', {'items': items})

@login_required
def experience_create(request):
    return handle_crud(request, Experience, ExperienceForm, None, 'core/experience_form.html', 'experience_list')

@login_required
def experience_edit(request, pk):
    return handle_crud(request, Experience, ExperienceForm, None, 'core/experience_form.html', 'experience_list', pk=pk)

@login_required
def experience_delete(request, pk):
    return handle_crud(request, Experience, ExperienceForm, None, None, 'experience_list', pk=pk, delete=True)

# --- Skills CRUD ---
@login_required
def skill_list(request):
    items = Skill.objects.all()
    return render(request, 'core/skill_list.html', {'items': items})

@login_required
def skill_create(request):
    return handle_crud(request, Skill, SkillForm, None, 'core/skill_form.html', 'skill_list')

@login_required
def skill_edit(request, pk):
    return handle_crud(request, Skill, SkillForm, None, 'core/skill_form.html', 'skill_list', pk=pk)

@login_required
def skill_delete(request, pk):
    return handle_crud(request, Skill, SkillForm, None, None, 'skill_list', pk=pk, delete=True)

# --- Certifications CRUD ---
@login_required
def certification_list(request):
    items = Certification.objects.all()
    return render(request, 'core/certification_list.html', {'items': items})

@login_required
def certification_create(request):
    return handle_crud(request, Certification, CertificationForm, None, 'core/certification_form.html', 'certification_list')

@login_required
def certification_edit(request, pk):
    return handle_crud(request, Certification, CertificationForm, None, 'core/certification_form.html', 'certification_list', pk=pk)

@login_required
def certification_delete(request, pk):
    return handle_crud(request, Certification, CertificationForm, None, None, 'certification_list', pk=pk, delete=True)

# --- Projects CRUD ---
@login_required
def project_list(request):
    items = Project.objects.all()
    return render(request, 'core/project_list.html', {'items': items})

@login_required
def project_create(request):
    return handle_crud(request, Project, ProjectForm, None, 'core/project_form.html', 'project_list')

@login_required
def project_edit(request, pk):
    return handle_crud(request, Project, ProjectForm, None, 'core/project_form.html', 'project_list', pk=pk)

@login_required
def project_delete(request, pk):
    return handle_crud(request, Project, ProjectForm, None, None, 'project_list', pk=pk, delete=True)

# --- Blogs CRUD ---
@login_required
def blog_list(request):
    items = BlogPost.objects.all()
    return render(request, 'core/blog_list.html', {'items': items})

@login_required
def blog_create(request):
    return handle_crud(request, BlogPost, BlogPostForm, None, 'core/blog_form.html', 'blog_list')

@login_required
def blog_edit(request, pk):
    return handle_crud(request, BlogPost, BlogPostForm, None, 'core/blog_form.html', 'blog_list', pk=pk)

@login_required
def blog_delete(request, pk):
    return handle_crud(request, BlogPost, BlogPostForm, None, None, 'blog_list', pk=pk, delete=True)
