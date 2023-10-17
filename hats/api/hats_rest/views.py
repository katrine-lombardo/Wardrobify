from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
import json
from common.json import ModelEncoder

from .models import Hat
# Create your views here.

class HatListEncoder(ModelEncoder):
    model = Hat
    properties = ["style"]

class HatDetailEncoder(ModelEncoder):
    model = Hat
    properties = [
        "color",
        "style",
        "size",
        "brand"
    ]


def api_list_hats(request, pk)
