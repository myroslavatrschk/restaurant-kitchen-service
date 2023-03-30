from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic

from foodie.models import Dish, DishType, Cook


def index(request):
    num_dishes = Dish.objects.count()
    num_dishtypes = DishType.objects.count()
    num_cooks = Cook.objects.count()

    context = {
        "num_dishes": num_dishes,
        "num_dishtypes": num_dishtypes,
        "num_cooks": num_cooks,
    }

    return render(request, "foodie/index.html", context=context)


class DishTypeListView(generic.ListView):
    model = DishType
    context_object_name = "dish_type_list"
    template_name = "foodie/dish_type_list.html"
    queryset = DishType.objects.order_by("name")
    paginate_by = 10


class DishListView(generic.ListView):
    model = Dish
    paginate_by = 10
    queryset = Dish.objects.select_related("dish_type")


class DishDetailView(generic.DetailView):
    model = Dish


class CookListView(generic.ListView):
    model = Cook
    paginate_by = 10


class CookDetailView(generic.DetailView):
    model = Cook
    queryset = Cook.objects.prefetch_related("dishes__dish_type")
