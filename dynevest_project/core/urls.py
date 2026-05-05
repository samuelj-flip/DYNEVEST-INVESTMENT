from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Access your database manager here
    path('admin/', admin.site.urls), 
    
    # This sends all traffic starting with 'accounts/' to the accounts app
    path('accounts/', include('accounts.urls')), 
]