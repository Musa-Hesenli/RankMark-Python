from django.urls import path
from .views import *
urlpatterns = [
    path("categories", CategoryAPIView.as_view()),
    path("hotels", HotelsAPIView.as_view())
]