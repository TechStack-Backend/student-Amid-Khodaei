from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='Home'),
    path('Developers/', views.Developers, name='Developers'),
    path('Projects/', views.Projects),
    path('add_developer/', views.add_developer),
    path('add_project/', views.add_project)
]
