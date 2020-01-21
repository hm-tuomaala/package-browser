from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:key>/', views.browse, name='package_page'),
]
