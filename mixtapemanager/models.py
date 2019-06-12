from django.db import models

# Create your models here.

class Mixtape(models.Model):
    mixtape_name = models.CharField(max_length=255)