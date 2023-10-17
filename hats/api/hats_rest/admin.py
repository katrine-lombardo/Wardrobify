from django.contrib import admin
from .models import LocationVO
# Register your models here.


@admin.register(LocationVO)
class LocationVOAdmin(admin.ModelAdmin):
    pass
