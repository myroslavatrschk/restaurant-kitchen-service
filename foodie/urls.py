from django.urls import path

from foodie.views import index

urlpatterns = [
    path("", index, name="index"),
]

app_name = "foodie"
