from django.urls import path
from . import views

urlpatterns = [    
    path('rebase/home', views.home, name='home'),
    path('logout', views.logout),
]