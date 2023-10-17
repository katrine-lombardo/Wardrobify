from django.db import models


class Hat(models.Model):
    brand = models.CharField(max_length=150)
    style = models.CharField(max_length=150)
    color = models.CharField(max_length=150)
    size = models.SmallIntegerField()
