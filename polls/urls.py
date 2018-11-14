from django.urls import path

from . import views


urlpatterns = [
    path('newpage/', views.newPage, name='newPage'),
    path('', views.index, name='index')
]
