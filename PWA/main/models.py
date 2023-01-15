from django.db import models

# Create your models here.
class menu(models.Model):
    item = models.CharField(max_length=255)
    price = models.IntegerField()
    