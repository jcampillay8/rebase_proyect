from django.urls import path
from . import views

urlpatterns = [    
    path('rebase/home', views.home, name='home'),
    path('logout', views.logout),
    path('rebase/add_text', views.add_text, name='add_text'),
    path('rebase/add_text2', views.add_text2, name='add_text2'),
    path('rebase/read', views.read, name='read'),
    path('rebase/word', views.word, name='word'),
    path('rebase/phrase', views.phrase, name='phrase'),
    path('rebase/contact', views.contact, name='contact'),
    path('rebase/success2', views.success2, name='success2'),
    path('rebase/users', views.users, name="users"),
]