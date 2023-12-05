from django.shortcuts import render

def index(request):
    """The home page for Learning Log app."""
    return render(request, "learning_logs/index.html")