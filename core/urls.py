from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('reserve/', views.reserve, name='reserve'),
    path('menu/', views.menu, name='menu'),
    path('gallery/', views.gallery, name='gallery'),
    path('team/', views.team, name='team'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
]
