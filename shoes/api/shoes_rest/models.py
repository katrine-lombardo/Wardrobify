from django.db import models
from django.urls import reverse

# Create your models here.

class BinVO(models.Model):
    import_href = models.CharField(max_length=200, unique=True)

    closet_name = models.CharField(max_length=100)
    bin_number = models.PositiveSmallIntegerField()
    bin_size = models.PositiveSmallIntegerField()


class Shoe(models.Model):
    brand = models.CharField(max_length=150)
    size = models.PositiveSmallIntegerField(primary_key=True)
    colour = models.CharField(max_length=150)
    style = models.CharField(max_length=150)
    bin = models.ForeignKey(
        BinVO,
        related_name="shoes",
        on_delete=models.CASCADE,
    )
