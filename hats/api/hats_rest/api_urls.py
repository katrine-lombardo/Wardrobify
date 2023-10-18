from django.urls import path

from hats_rest.api_views import (
    api_list_hats,
    api_view_hat)


urlpatterns = [
    path("hats/", api_list_hats, name="api_list_hats"),
    path("hats/<int:pk>/", api_view_hat, name="api_view_hat"),
]
