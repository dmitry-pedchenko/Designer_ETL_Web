from django.urls import path, include
from .views import get_info, get_list_configs
urlpatterns = [
    path('get/<str:name>/<str:mode>', get_info),
    path('open', get_list_configs)
]
