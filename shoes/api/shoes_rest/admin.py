from django.contrib import admin
from .models import BinVO

# Register your models here.

@admin.register(BinVO)
class BinVOAdmin(admin.ModelAdmin):
    pass
