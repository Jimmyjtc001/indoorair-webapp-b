from django.urls import path

from . import views

urlpatterns = [
    path('retrieve', views.retrieve_page, name='retrieve_page'),
    path('api/retrieve1',views.retrieve_api, name = 'retrieve_api'),

]
