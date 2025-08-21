from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home),
    path('Developers/', views.Developers),
    path('Developers/CV/<int:cv_id>/', views.CV)
]
