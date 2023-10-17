from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
import json

from common.json import ModelEncoder
from .models import Shoe

# Create your views here.





class ShoeListEncoder(ModelEncoder):
    model = Shoe
    properties = [
        "style"
        ]


class ShoeDetailEncoder(ModelEncoder):
    model = Shoe
    properties = [
        "style",
        "colour",
        "size",
        "brand",
    ]

@require_http_methods(["GET", "POST"])
def api_list_shoes(request):
