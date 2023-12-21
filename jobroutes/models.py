from django.db import models
from django.db.models import CharField

class JobRoutes(models.Model):
    name = CharField(max_length=255)
    founder = CharField(max_length=255)
    about = models.TextField()

