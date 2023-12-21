from django.db import models
from django.db.models import CharField

class BootCamp(models.Model):
    name = CharField(max_length=255)
    teachers = CharField(max_length=255)
    about = models.TextField()
    price = models.IntegerField()

