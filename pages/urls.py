from django.urls import path
from . import views
urlpatterns = [
    path('throw_utilities/', views.throw_utilities),
    path('static_example/', views.static_example),
    path('catch/', views.catch),
    path('throw/', views.throw),
    path('birth/', views.birth),
    path('template_language/', views.template_language),
    path('greeting/<str:name>/', views.greeting),

    path('index/', views.index),
    path('dinner/', views.dinner),

]