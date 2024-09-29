from django.urls import path
from .views import *

urlpatterns = [
    path("", homePages, name="home")
]
