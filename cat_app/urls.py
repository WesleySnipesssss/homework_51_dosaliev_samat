from django.urls import path
from . import views

urlpatterns = [
    path("", views.welcome, name="welcome"),
    path("cat_info/", views.cat_info, name="cat_info"),
]
