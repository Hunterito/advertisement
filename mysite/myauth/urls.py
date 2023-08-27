from django.urls import path
from .views import my_login, profile, my_register, my_logout

urlpatterns = [
    path("myauth/", my_login, name="login"),
    path("profile/", profile, name="profile"),
    path("register/", my_register, name="register"),
    path("#", my_logout, name="logout")
]
