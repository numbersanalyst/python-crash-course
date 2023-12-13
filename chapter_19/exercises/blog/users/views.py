from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render


def register(request):
    """Register a new user, generate form or process form."""
    if request.method != "POST":
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            user_data = form.save()
            login(request, user_data)
            return redirect("blogs:index")

    context = {"form": form}
    return render(request, "registration/register.html", context)
