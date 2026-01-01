from django.urls import path, include
from rest_framework.routers import DefaultRouter
from whatido.views import ServiceViewSet
from testimonials.views import TestimonialViewSet
from experience.views import ExperienceViewSet
from skills.views import SkillViewSet
from certifications.views import CertificationViewSet
from projects.views import ProjectViewSet
from blogs.views import BlogPostViewSet

router = DefaultRouter()
router.register(r'whatido', ServiceViewSet)
router.register(r'testimonials', TestimonialViewSet)
router.register(r'experience', ExperienceViewSet)
router.register(r'skills', SkillViewSet)
router.register(r'certifications', CertificationViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'blogs', BlogPostViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
