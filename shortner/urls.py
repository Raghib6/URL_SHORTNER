from django.urls import path
from shortner import views

urlpatterns = [
    path('', views.homepage, name='home')
]
