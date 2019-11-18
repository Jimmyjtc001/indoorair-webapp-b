
from django.urls import path

from . import views

urlpatterns = [
    path('login', views.login_page, name='login_page'),
    path('register',views.register_page, name = 'register_page'),
    path('register/success',views.register_success_page, name = 'register_success_page'),
    path('api/login',views.post_login_api, name = 'login_api'),
    path('api/register',views.post_register_api, name = 'register_api'),
    path('api/logout',views.post_logout_api, name = 'logout_api'),
    ]
