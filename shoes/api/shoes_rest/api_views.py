from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
import json

from common.json import ModelEncoder
from .models import Shoe, BinVO

# Create your views here.


class BinVODetailEncoder(ModelEncoder):
    model = BinVO
    properties = [
        "closet_name",
        "import_href"
    ]


class ShoeListEncoder(ModelEncoder):
    model = Shoe
    properties = [
        "model_name"
        ]

    def get_extra_data(self, o):
        return {"bin": o.bin.closet_name}


class ShoeDetailEncoder(ModelEncoder):
    model = Shoe
    properties = [
        "manufacturer",
        "picture_url",
        "colour",
        "model_name",
        "bin"
    ]
    encoders = {
        "bin": BinVODetailEncoder(),
    }


@require_http_methods(["GET", "POST"])
def api_list_shoes(request, bin_vo_id=None):
    if request.method == "GET":
        shoes = Shoe.objects.filter(bin=bin_vo_id)
        if bin_vo_id is not None:
            shoes = Shoe.objects.filter(bin=bin_vo_id)
        else:
            shoes = Shoe.objects.all()
        return JsonResponse(
            {"shoes": shoes},
            encoder=ShoeListEncoder,
        )
    else:
        content = json.loads(request.body)
        try:
            bin_href = content["bin"]
            bin_id = f"/api/bins/{bin_href}/"
            bin = BinVO.objects.get(import_href=bin_id)
            content["bin"] = bin
        except BinVO.DoesNotExist:
            return JsonResponse(
                {"message": "Invalid bin id"},
                status=400,
            )

        shoe = Shoe.objects.create(**content)
        return JsonResponse(
            shoe,
            encoder=ShoeDetailEncoder,
            safe=False,
        )

def api_show_shoe(request, pk):
    shoe = Shoe.objects.get(id=pk)
    return JsonResponse(
        shoe,
        encoder=ShoeDetailEncoder,
        safe=False,
    )
