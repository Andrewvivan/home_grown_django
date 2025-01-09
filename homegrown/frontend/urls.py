from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),         # Serves the homepage ("/")
    path('about/', views.about, name='about'),  # Serves "/about/"
    path('contact/', views.contact, name='contact'),  # Serves "/contact/"
    path('homegrown/', views.index, name='homegrown'),  # Serves "/homegrown/"
]
