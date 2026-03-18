from django.urls import path
from django.http import HttpRequest, HttpResponse


def index(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Hello, world!")


urlpatterns = [
    path("", index),
]
