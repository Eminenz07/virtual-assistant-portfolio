from django.contrib import admin
from .models import Certification

@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ('title', 'issuer', 'date_earned')
    list_filter = ('issuer', 'date_earned')
    search_fields = ('title', 'issuer')
