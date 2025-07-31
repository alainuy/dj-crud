from django.urls import path
from . import views

urlpatterns = [
    path('', views.employee_list),
    path('new/', views.employee_form),
    path('new/<int:id>', views.employee_form, name='edit_employee'),
]