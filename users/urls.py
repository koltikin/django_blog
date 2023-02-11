from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("register/", views.register, name="register"),
    path("login/", views.LoginLogout.login_form, name="login"),
    path("logout/", views.LoginLogout.logout_form, name="logout"),
    path("profile/", views.Profile, name="profile"),
    path(
        "password_reset/",
        auth_views.PasswordResetView.as_view(template_name="users/pssword_reset.html"),
        name="password_reset",
    ),
    path(
        "password_reset/done",
        auth_views.PasswordResetDoneView.as_view(
            template_name="users/pssword_reset_done.html"
        ),
        name="password_reset_done",
    ),
    path(
        "password_reset_confirm/<uidb64>/<token>",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="users/pssword_reset_confirm.html"
        ),
        name="password_reset_confirm",
    ),
]
