from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path('calendar/', views.calendar_view, name='calendar_view'),
    path('add/<str:date>/', views.add_expense_view, name='add_expense'),
]