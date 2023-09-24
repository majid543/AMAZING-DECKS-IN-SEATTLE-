from django.contrib import admin
from django.urls import path,include
from . import views

app_name ="app"

urlpatterns = [
    path('quote',views.CustomersCreateView.as_view(), name = 'quote'),
    path('home',views.homeview, name = 'home'),
    path('',views.homeview, name = 'home'),
    path('policy', views.policy_view, name='Policy'),
    path('gallery', views.gallery_view, name='gallery'),
    path('schedule',views.CustomersCreateView.as_view(), name = 'schedule'),
    path('area', views.area_view, name='area'),
    path('fetch_project_photos/<int:project_id>/', views.fetch_project_photos, name='fetch_project_photos'),
]

