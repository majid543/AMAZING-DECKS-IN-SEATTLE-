from django.urls import path
from . import views



app_name = "estimate"
urlpatterns = [
    path('calculate-charges/', views.calculate_charges, name='calculate-charges'),
    path('quoe',views.customers_create_view, name = 'quoe'),
    path('quo',views.customers_create_view, name = 'quo'),
]