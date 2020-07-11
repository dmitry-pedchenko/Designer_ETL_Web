from django.urls import path, include
from .views import get_info
urlpatterns = [
    path('get/<str:name>/<str:mode>', get_info)
]
