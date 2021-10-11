from django.urls import path
from shortner import views

urlpatterns = [
    path('', views.homepage, name='home'),
    path('create', views.create, name='create'),
    path('<str:pk>', views.go, name='go')
]
