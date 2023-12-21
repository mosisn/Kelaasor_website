from django.contrib.admin import ModelAdmin, register
from .models import BootCamp

@register(BootCamp)
class BootCampAdmin(ModelAdmin):
    pass
