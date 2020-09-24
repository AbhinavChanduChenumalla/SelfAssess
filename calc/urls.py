from django.urls import path
from . import views
from django.conf import settings

urlpatterns = [
    path('',views.home,name='home'),
    path('input',views.input,name='input'),
    path('previous',views.previous,name='previous'),
    path('profile',views.profile,name='profile'),
    path('profile_update',views.profile_update,name='profile_update'),
    path('profile_update_action',views.profile_update_action,name='profile_update_action'),
    path('query',views.query,name='query'),
    path('updateTests',views.updateTests,name='updateTests'),
    path('testDetails',views.testDetails,name='testDetails'),
]
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)