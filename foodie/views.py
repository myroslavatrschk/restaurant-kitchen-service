from django.http import HttpResponse
from django.shortcuts import render

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
