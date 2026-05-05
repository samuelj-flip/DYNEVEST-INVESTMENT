from django.urls import path
from . import views 

urlpatterns = [
    path('index/', views.index, name='index'),
    path('plans/', views.plans_view, name='plans'),
    path('transactions/', views.transactions_view, name='transactions'),
    path('settings/', views.settings_view, name='settings'),
]