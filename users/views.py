from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views


# Create your views here.


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
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
    password_reset = auth_views.PasswordResetView.as_view(
        template_name="users/pssword_reset.html"
    )
    password_reset_done = auth_views.PasswordResetDoneView.as_view(
        template_name="users/pssword_reset_done.html"
    )
    password_reset_confirm = auth_views.PasswordResetConfirmView.as_view(
        template_name="users/pssword_reset_confirm.html"
    )

    password_reset_complete = auth_views.PasswordResetCompleteView.as_view(
        template_name="users/pssword_reset_complete.html"
    )


@login_required
def Profile(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile
        )
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, "Your account has been updated")
            return redirect("profile")
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {"u_form": u_form, "p_form": p_form}
    return render(request, "users/profile.html", context)
