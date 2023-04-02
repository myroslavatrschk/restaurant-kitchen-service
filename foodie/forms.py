from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms

from foodie.models import Cook, Dish
from foodie.validators import experience_validator, price_validator


class CookCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Cook
        fields = UserCreationForm.Meta.fields + (
            "email",
            "first_name",
            "last_name",
            "years_of_experience"
        )

    def clean_years_of_experience(self):
        years_of_experience = self.cleaned_data["years_of_experience"]
        return experience_validator(years_of_experience)


class CookUpdateForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Cook
        fields = UserCreationForm.Meta.fields + (
            "email",
            "first_name",
            "last_name",
            "years_of_experience"
        )

    def clean_years_of_experience(self):
        years_of_experience = self.cleaned_data["years_of_experience"]
        return experience_validator(years_of_experience)


class DishForm(forms.ModelForm):
    cooks = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    class Meta:
        model = Dish
        fields = "__all__"

    def clean_price(self):
        price = self.cleaned_data["price"]
        return price_validator(price)


class DishSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={"placeholder": "Search by dish name..."}
        ),
    )


class CookSearchForm(forms.Form):
    username = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={"placeholder": "Search by username..."}
        ),
    )


class DishTypeSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={"placeholder": "Search by dish type name..."}
        ),
    )
