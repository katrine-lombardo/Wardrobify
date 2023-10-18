from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
import json
from common.json import ModelEncoder

from .models import Hat, LocationVO
# Create your views here.


class LocationVODetailEncoder(ModelEncoder):
    model = LocationVO
    properties = [
        "closet_name",
        "import_href"
    ]


class HatListEncoder(ModelEncoder):
    model = Hat
    properties = ["style"]

    def get_extra_data(self, o):
        return {"location": o.location.closet_name}


class HatDetailEncoder(ModelEncoder):
    model = Hat
    properties = [
        "color",
        "style",
        "fabric",
        "picture_url",
        "location",
    ]
    encoders = {
        "location": LocationVODetailEncoder(),
    }


@require_http_methods(["GET", "POST"])
def api_list_hats(request, location_vo_id=None):
    if request.method == "GET":
        hats = Hat.objects.filter(location=location_vo_id)
        if location_vo_id is not None:
            hats = Hat.objects.filter(location=location_vo_id)
        else:
            hats = Hat.objects.all()
        return JsonResponse(
            {"hats": hats},
            encoder=HatListEncoder
        )
    else:
        content = json.loads(request.body)

        try:
            location_href = content["location"]
            location_id = f"/api/locations/{location_href}/"
            location = LocationVO.objects.get(import_href=location_id)
            content["location"] = location
        except LocationVO.DoesNotExist:
            return JsonResponse(
                {"message": "Invalid location id"},
                status=400,
            )

        hat = Hat.objects.create(**content)
        return JsonResponse(
            hat,
            encoder=HatDetailEncoder,
            safe=False,
        )


def api_view_hat(request, pk):
    hat = Hat.objects.get(id=pk)
    return JsonResponse(
        hat,
        encoder=HatDetailEncoder,
        safe=False,
    )
