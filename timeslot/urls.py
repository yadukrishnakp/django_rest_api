from django.urls import path
from . import views

urlpatterns = [
    path('', views.RegisterList, name="register_list"),
    path('user_register/', views.User_Register, name="user_register")
]