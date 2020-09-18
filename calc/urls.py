from django.urls import path

from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('input',views.input,name='input'),
    path('previous',views.previous,name='previous'),
    path('profile',views.profile,name='profile'),
    path('profile_update',views.profile_update,name='profile_update'),
    path('profile_update_action',views.profile_update_action,name='profile_update_action'),
    path('query',views.query,name='query'),
]