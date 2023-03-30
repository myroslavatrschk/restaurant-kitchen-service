from django.urls import path

from foodie.views import (
    index,
    DishListView,
    DishDetailView,
    CookListView,
    CookDetailView,
    DishTypeListView
)

urlpatterns = [
    path("", index, name="index"),
    path("dishes/", DishListView.as_view(), name="dishes"),
    path("dishes/<int:pk>", DishDetailView.as_view(), name="dish-detail"),
    path("cooks/", CookListView.as_view(), name="cooks"),
    path("cooks/<int:pk>", CookDetailView.as_view(), name="cook-detail"),
    path("dish-types/", DishTypeListView.as_view(), name="dish-type-list"),
]

app_name = "foodie"
