from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views


# Create your views here.


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(
                request, "Your account has been created! You are now able to log in"
            )
            return redirect("login")
    else:
        form = UserRegisterForm()

    return render(request, "users/register.html", {"form": form, "title": "Register"})


class LoginLogout:
    login_form = auth_views.LoginView.as_view(template_name="users/login.html")
    logout_form = auth_views.LogoutView.as_view(template_name="users/logout.html")


@login_required
def Profile(request):
    return render(request, "users/profile.html")
