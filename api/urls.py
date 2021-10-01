from django.urls import path
from api import views

url_patterns = [
    path('gather/', views.create_view),
]