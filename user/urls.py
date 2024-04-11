from django.urls import path
from .views import user_create_view, user_login_view

urlpatterns = [
    path(
        "create/",
        user_create_view.create_user,
        name="create_user",
    ),
    path(
        "login/",
        user_login_view.login_user,
        name="login_user"
    )
]
