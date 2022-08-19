from django.urls import URLPattern, path
from . import views

urlpatterns = [
    
    path('', views.create, name='create'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('delete_mode/<int:id>/', views.delete_mode, name='delete_mode'),
    path('add/', views.add, name='add'),
]