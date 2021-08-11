from django.urls import path
from django.conf import  settings
from django.conf.urls.static import static

from . import views

app_name='chat_login'

urlpatterns = [
    path('', views.log_in, name='log_in'),
    path('registration/', views.sign_up, name='sign_up'),
    path('logout/', views.log_out, name='log_out'),

    path('index/', views.Index.as_view(), name='index'),
    path('groups/', views.Groups.as_view(), name='groups'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)