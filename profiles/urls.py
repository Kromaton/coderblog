from django.contrib import admin
from django.urls import path
from profiles.views import (registro, login_view, CustomLogoutView, ProfileUpdateView, agregar_avatar)


urlpatterns = [
    # URLS Usuario y sesion
    path('', registro, name="registro"),
    path('login/', login_view, name="login"),
    path('profile/', ProfileUpdateView.as_view(), name="perfil"),
    path('logout/', CustomLogoutView.as_view(), name="logout"),
    path('avatar/', agregar_avatar, name="avatar"),
]