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
        "id",
        "manufacturer",
        "picture_url",
        "colour",
        "model_name",
        "bin"
        ]

    def get_extra_data(self, o):
        return {"bin": o.bin.closet_name}


class ShoeDetailEncoder(ModelEncoder):
    model = Shoe
    properties = [
        "id",
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
        if bin_vo_id is not None:
            shoes = Shoe.objects.filter(bin=bin_vo_id)
        else:
            shoes = Shoe.objects.all()
        return JsonResponse(
            {"shoes": shoes},
            encoder=ShoeDetailEncoder,
        )
    else:
        content = json.loads(request.body)
        try:
            bin_id = content["bin"]
            bin_href = f"/api/bins/{bin_id}/"
            bin = BinVO.objects.get(import_href=bin_href)
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


@require_http_methods(["GET", "PUT", "DELETE"])
def api_show_shoe(request, pk):
    if request.method == "GET":
        shoe = Shoe.objects.get(id=pk)
        return JsonResponse(
            shoe,
            encoder=ShoeDetailEncoder,
            safe=False,
        )
    elif request.method == "DELETE":
        count, _ = Shoe.objects.filter(id=pk).delete()
        return JsonResponse({"deleted": count > 0})
    else:
        content = json.loads(request.body)
        try:
            if "bin" in content:
                bin = BinVO.objects.get(id=content["bin"])
                content["bin"] = bin
        except BinVO.DoesNotExist:
            return JsonResponse(
                {"message": "Invalid bin id"},
                status=400,
            )

        Shoe.objects.filter(id=pk).update(**content)
        shoe = Shoe.objects.get(id=pk)
        return JsonResponse(
            shoe,
            encoder=ShoeDetailEncoder,
            safe=False,
        )
