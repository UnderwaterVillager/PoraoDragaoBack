from django.urls import path
from . import views

urlpatterns = [
    path("userpage/", views.display_user),
]
