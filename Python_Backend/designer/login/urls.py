from django.urls import path, include
from .views import login_designer
urlpatterns = [
    path('post/login', login_designer)
    ]