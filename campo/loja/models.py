from django.db import models
from django.utils import timezone

class Produto(models.Model):
    nome = models.CharField(max_lenght=200)
    descrcao = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

# Create your models here.
