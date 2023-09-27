from django.urls import path 
from .views import index, spot_detail

urlpatterns = [
    path('', index, name="index"),
    path('spot/<str:pk>/', spot_detail, name="spot-detail"),
]