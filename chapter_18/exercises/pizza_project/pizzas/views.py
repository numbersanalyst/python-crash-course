from django.shortcuts import render

from .models import Pizza


def index(request):
    """Render the index page for the pizza app."""
    return render(request, "pizzas/index.html")


def pizzas(request):
    """Show all pizzas."""
    all_pizzas = Pizza.objects.order_by("name")
    context = {
        "pizzas": all_pizzas,
    }
    return render(request, "pizzas/pizzas.html", context)


def pizza(request, pizza_id):
    """Show a single pizza and all toppings."""
    pizza = Pizza.objects.get(id=pizza_id)
    pizza_toppings = pizza.topping_set.order_by("-date_added")
    context = {"pizza": pizza, "toppings": pizza_toppings}
    return render(request, "pizzas/pizza.html", context)
