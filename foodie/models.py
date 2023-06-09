from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class Dish(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=7, decimal_places=2)
    dish_type = models.ForeignKey(
        "DishType",
        on_delete=models.CASCADE,
        related_name="dishes"
    )
    cooks = models.ManyToManyField("Cook", related_name="dishes")

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Cook(AbstractUser):
    years_of_experience = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Cook"
        verbose_name_plural = "Cooks"


class DishType(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name
