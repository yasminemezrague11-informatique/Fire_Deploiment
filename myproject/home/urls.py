from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index , name='index'),
    path('consignes/', views.consignes, name='consignes'),
    path('connexion/', views.connexion, name='connexion'), 
    path('propos/', views.propos, name='propos'),
    path('declare_fire/', views.declare_fire, name='declare_fire'),
    path('register/', views.register, name='register'),
    path('api/incendies', views.incendies_api, name='incendies_api'),
]

