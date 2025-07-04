from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('api/tracker/', views.tracker_data, name='tracker_data'),
    path('api/badge/', views.badge_json, name='badge_json'),
]
