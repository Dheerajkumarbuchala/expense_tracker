from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.main_visualization_view, name='main_visualization'),
    path('daily-expenses-by-category/', views.daily_expenses_by_category_view, name='daily_expenses_by_category'),
    path('reports/', views.reports_view, name='reports'),
    path('report-data/', views.report_data, name='report_data'),
]