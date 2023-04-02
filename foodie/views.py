from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic

from foodie.forms import CookUpdateForm, CookCreationForm, CookSearchForm, DishSearchForm, DishTypeSearchForm, DishForm
from foodie.models import Dish, DishType, Cook


@login_required
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


class DishTypeListView(LoginRequiredMixin, generic.ListView):
    model = DishType
    context_object_name = "dish_type_list"
    template_name = "foodie/dishtype_list.html"
    queryset = DishType.objects.order_by("name")
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(DishTypeListView, self).get_context_data(**kwargs)
        name = self.request.GET.get("name", "")
        context["search_form"] = DishTypeSearchForm(
            initial={"name": name}
        )
        return context

    def get_queryset(self):
        queryset = DishType.objects.all()
        form = DishTypeSearchForm(self.request.GET)

        if form.is_valid():
            return queryset.filter(
                name__icontains=form.cleaned_data["name"]
            )
        return queryset


class DishTypeCreateView(LoginRequiredMixin, generic.CreateView):
    model = DishType
    fields = "__all__"
    success_url = reverse_lazy("foodie:dish-type-list")


class DishTypeUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = DishType
    fields = "__all__"
    success_url = reverse_lazy("foodie:dish-type-list")


class DishTypeDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = DishType
    success_url = reverse_lazy("foodie:dish-type-list")


class DishListView(LoginRequiredMixin, generic.ListView):
    model = Dish
    paginate_by = 5
    queryset = Dish.objects.select_related("dish_type")

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(DishListView, self).get_context_data(**kwargs)
        name = self.request.GET.get("name", "")
        context["search_form"] = DishSearchForm(
            initial={"name": name}
        )
        return context

    def get_queryset(self):
        queryset = Dish.objects.all()
        form = DishSearchForm(self.request.GET)

        if form.is_valid():
            return queryset.filter(
                name__icontains=form.cleaned_data["name"]
            )
        return queryset


class DishDetailView(LoginRequiredMixin, generic.DetailView):
    model = Dish


class DishCreateView(LoginRequiredMixin, generic.CreateView):
    model = Dish
    fields = DishForm
    success_url = reverse_lazy("foodie:dishes")


class DishUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Dish
    fields = DishForm
    success_url = reverse_lazy("foodie:dishes")


class DishDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Dish
    success_url = reverse_lazy("foodie:dishes")


class CookListView(LoginRequiredMixin, generic.ListView):
    model = Cook
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CookListView, self).get_context_data(**kwargs)
        username = self.request.GET.get("username", "")
        context["search_form"] = CookSearchForm(
            initial={"username": username}
        )
        return context

    def get_queryset(self):
        queryset = Cook.objects.all()
        form = CookSearchForm(self.request.GET)

        if form.is_valid():
            return queryset.filter(
                username__icontains=form.cleaned_data["username"]
            )
        return queryset


class CookDetailView(LoginRequiredMixin, generic.DetailView):
    model = Cook
    queryset = Cook.objects.prefetch_related("dishes__dish_type")


class CookCreateView(LoginRequiredMixin, generic.CreateView):
    model = Cook
    form_class = CookCreationForm
    success_url = reverse_lazy("foodie:cooks")


class CookUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Cook
    form_class = CookUpdateForm
    success_url = reverse_lazy("foodie:cooks")


class CookDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Cook
    success_url = reverse_lazy("foodie:cooks")


def assign_delete_cook(request, pk):
    user = request.user
    dish = Dish.objects.get(pk=pk)
    if user in dish.cooks.all():
        dish.cooks.remove(user)
    else:
        dish.cooks.add(user)
    return redirect("foodie:dish-detail", pk)


def assign_delete_dish(request, pk):
    user = request.user
    cook = Cook.objects.get(pk=pk)
    if user in cook.dishes.all():
        cook.dishes.remove(user)
    else:
        cook.dishes.add(user)
    return redirect("foodie:cook-detail", pk)
