from django.urls import path, include
from .views import dashboard, profile_list, profile, register, login

app_name = "socnet"

urlpatterns = [
    path("accounts/", include("django.contrib.auth.urls")),
    path("", dashboard, name="dashboard"),
    path('profile_list/', profile_list, name='profile_list'),
    path('profile/<int:pk>', profile, name='profile'),
    path('register/', register, name='register')
]