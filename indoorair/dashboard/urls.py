from django.urls import path

from . import views

urlpatterns = [
    path('dashboard', views.dashboard_page, name='dashboard_page'),
    path('api/dashboard', views.get_dashboard_api, name='dashboard_apis'),
    path('api/dashboard_aprove', views.DashboardAproveApi.as_view()),
]
