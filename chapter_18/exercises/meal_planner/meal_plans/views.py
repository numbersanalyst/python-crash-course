from django.shortcuts import render

def index(request):
    """Render the index page for the meal planner app."""
    return render(request, "meal_plans/index.html")