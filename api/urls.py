from django.urls import path
from . import views

urlpatterns = [
    path('machines', views.machine_list, name='machine-list'),
    path('machines/<int:id>', views.machine, name='machine-detail'),
    path('module/<int:id>', views.module, name='module-detail'),
]