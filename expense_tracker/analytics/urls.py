from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.main_visualization_view, name='main_visualization'),
    path('daily-expenses-by-category/', views.daily_expenses_by_category_view, name='daily_expenses_by_category'),
    path('daily-expenses-in-month/', views.daily_expenses_in_month_view, name='daily_expenses_in_month'),
    path('monthly-expenses-in-year/', views.monthly_expenses_in_year_view, name='monthly_expenses_in_year'),
]