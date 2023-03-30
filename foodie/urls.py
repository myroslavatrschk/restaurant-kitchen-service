from django.urls import path

from foodie.views import (
    index,
    DishListView,
    DishDetailView,
    DishCreateView,
    DishUpdateView,
    DishDeleteView,
    CookListView,
    CookDetailView,
    DishTypeListView,
    DishTypeCreateView,
    DishTypeUpdateView,
    DishTypeDeleteView, CookCreateView, CookUpdateView, CookDeleteView, assign_delete_cook,
)

urlpatterns = [
    path("", index, name="index"),
    path("dishes/", DishListView.as_view(), name="dishes"),
    path("dishes/<int:pk>", DishDetailView.as_view(), name="dish-detail"),
    path(
        "dishes/create",
        DishCreateView.as_view(),
        name="dish-create"
    ),
    path(
        "dishes/<int:pk>/update",
        DishUpdateView.as_view(),
        name="dish-update"
    ),
    path(
        "dishes/<int:pk>/delete",
        DishDeleteView.as_view(),
        name="dish-delete"
    ),
    path("cooks/", CookListView.as_view(), name="cooks"),
    path("cooks/<int:pk>", CookDetailView.as_view(), name="cook-detail"),
    path("cooks/create", CookCreateView.as_view(), name="cook-create"),
    path("cooks/<int:pk>/update", CookUpdateView.as_view(), name="cook-update"),
    path("cooks/<int:pk>/delete", CookDeleteView.as_view(), name="cook-delete"),
    path("dish-types/", DishTypeListView.as_view(), name="dish-type-list"),
    path(
        "dish-types/create",
        DishTypeCreateView.as_view(),
        name="dish-type-create"
    ),
    path(
        "dish-types/<int:pk>/update",
        DishTypeUpdateView.as_view(),
        name="dish-type-update"
    ),
    path(
        "dish-types/<int:pk>/delete",
        DishTypeDeleteView.as_view(),
        name="dish-type-delete"
    ),
    path(
        "assign-delete-cook/<int:pk>",
        assign_delete_cook,
        name="assign-delete-cook"
    )
]

app_name = "foodie"
