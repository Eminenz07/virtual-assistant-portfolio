from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_home, name='dashboard_home'),
    path('login/', views.dashboard_login, name='login'),
    path('logout/', views.dashboard_logout, name='logout'),
    
    # Generic CRUD paths would be nice, but explicit is safer for now or use htmx patterns
    # What I Do
    path('services/', views.service_list, name='service_list'),
    path('services/create/', views.service_create, name='service_create'),
    path('services/<int:pk>/edit/', views.service_edit, name='service_edit'),
    path('services/<int:pk>/delete/', views.service_delete, name='service_delete'),

    # Testimonials
    path('testimonials/', views.testimonial_list, name='testimonial_list'),
    path('testimonials/create/', views.testimonial_create, name='testimonial_create'),
    path('testimonials/<int:pk>/edit/', views.testimonial_edit, name='testimonial_edit'),
    path('testimonials/<int:pk>/delete/', views.testimonial_delete, name='testimonial_delete'),

    # Experience
    path('experience/', views.experience_list, name='experience_list'),
    path('experience/create/', views.experience_create, name='experience_create'),
    path('experience/<int:pk>/edit/', views.experience_edit, name='experience_edit'),
    path('experience/<int:pk>/delete/', views.experience_delete, name='experience_delete'),

    # Skills
    path('skills/', views.skill_list, name='skill_list'),
    path('skills/create/', views.skill_create, name='skill_create'),
    path('skills/<int:pk>/edit/', views.skill_edit, name='skill_edit'),
    path('skills/<int:pk>/delete/', views.skill_delete, name='skill_delete'),

    # Certifications
    path('certifications/', views.certification_list, name='certification_list'),
    path('certifications/create/', views.certification_create, name='certification_create'),
    path('certifications/<int:pk>/edit/', views.certification_edit, name='certification_edit'),
    path('certifications/<int:pk>/delete/', views.certification_delete, name='certification_delete'),

    # Projects
    path('projects/', views.project_list, name='project_list'),
    path('projects/create/', views.project_create, name='project_create'),
    path('projects/<int:pk>/edit/', views.project_edit, name='project_edit'),
    path('projects/<int:pk>/delete/', views.project_delete, name='project_delete'),

    # Blogs
    path('blogs/', views.blog_list, name='blog_list'),
    path('blogs/create/', views.blog_create, name='blog_create'),
    path('blogs/<int:pk>/edit/', views.blog_edit, name='blog_edit'),
    path('blogs/<int:pk>/delete/', views.blog_delete, name='blog_delete'),
]
