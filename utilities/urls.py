from django.urls import path
from . import views
urlpatterns = [

path('utilities01/', views.utilities),
path('catch_utilities/', views.catch),
]