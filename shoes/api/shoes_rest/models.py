from django.db import models
from django.urls import reverse

# Create your models here.

class BinVO(models.Model):
    import_href = models.CharField(max_length=200, unique=True)

    closet_name = models.CharField(max_length=100)
    bin_number = models.PositiveSmallIntegerField()
    bin_size = models.PositiveSmallIntegerField()


class Shoe(models.Model):
    manufacturer = models.CharField(max_length=150)
    picture_url = models.URLField(null=True)
    colour = models.CharField(max_length=150)
    model_name = models.CharField(max_length=150)
    bin = models.ForeignKey(
        BinVO,
        related_name="shoes",
        on_delete=models.CASCADE,
    )
