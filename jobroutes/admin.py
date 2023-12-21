from django.contrib.admin import ModelAdmin, register
from .models import JobRoutes

@register(JobRoutes)
class JobroutesAdmin(ModelAdmin):
    pass