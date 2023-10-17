from django.db import models
from django.urls import reverse


class LocationVO(models.Model):
    import_href = models.CharField(max_length=200, unique=True)
    closet_name = models.CharField(max_length=100)
    section_number = models.PositiveSmallIntegerField()
    shelf_number = models.PositiveSmallIntegerField()


class Hat(models.Model):
    brand = models.CharField(max_length=150)
    style = models.CharField(max_length=150)
    color = models.CharField(max_length=150)
    size = models.PositiveSmallIntegerField(primary_key=True)
    location = models.ForeignKey(
        LocationVO,
        related_name="hats",
        on_delete=models.PROTECT,
    )
