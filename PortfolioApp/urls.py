from django.urls import path
from PortfolioApp import views


urlpatterns = [
    path('', views.index, name='index'),
]