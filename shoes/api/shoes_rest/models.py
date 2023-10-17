from django.db import models

# Create your models here.


class Shoe(models.Model):
    brand = models.CharField(max_length=150)
    size = models.PositiveSmallIntegerField(primary_key=True)
    colour = models.CharField(max_length=150)
    style = models.CharField(max_length=150)
