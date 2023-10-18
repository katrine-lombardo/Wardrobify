wdfrom django.urls import path

from hats_rest.api_views import (
    api_list_hats)


urlpatterns = [
    path("hats/", api_list_hats, name="api_list_hats")
]
