from django.urls import path
from . import views

urlpatterns =[
   path('', views.service, name='service'),
   path('conseil/', views.conseil, name='conseil'),

]
