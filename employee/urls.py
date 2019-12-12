from django.urls import path
from . import views

urlpatterns = [
    path('', views.employee_list),
    path('form/', views.employee_form)
]
