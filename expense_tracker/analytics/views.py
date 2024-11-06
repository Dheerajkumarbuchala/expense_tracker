from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from datetime import date, datetime
import json
from django.utils.safestring import mark_safe
import plotly # type: ignore
import plotly.express as px # type: ignore
from expenses.models import Expense
import pandas as pd

@login_required
def main_visualization_view(request):
    return render(request, 'analytics/main_visualization.html')


@login_required
def daily_expenses_by_category_view(request):
    today = date.today()
    expenses = Expense.objects.filter(user=request.user, date=today).values('category').annotate(total=Sum('amount'))
    data = [{'category': e['category'], 'amount': e['total']} for e in expenses]

    # Convert to DataFrame
    df = pd.DataFrame(data)

    # Handle case where there is no data for the day
    if df.empty:
        fig = px.pie(values=[1], names=["No Data"], title=f"No expenses for {today}")
    else:
        fig = px.pie(df, names='category', values='amount', title=f'Expenses for {today}')

    chart_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return render(request, 'analytics/daily_expenses_by_category.html', {'chart_json': mark_safe(chart_json)})


@login_required
def daily_expenses_in_month_view(request, month=None, year=None):
    month = month or datetime.today().month
    year = year or datetime.today().year
    expenses = Expense.objects.filter(user=request.user, date__year=year, date__month=month).values('date', 'category').annotate(total=Sum('amount'))
    data = [{'date': e['date'], 'category': e['category'], 'amount': e['total']} for e in expenses]

    fig = px.bar(data, x='date', y='amount', color='category', title=f'Daily Expenses for {year}-{month}')
    chart_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return render(request, 'analytics/daily_expenses_in_month.html', {'chart_json': mark_safe(chart_json)})


@login_required
def monthly_expenses_in_year_view(request, year=None):
    year = year or datetime.today().year
    expenses = Expense.objects.filter(user=request.user, date__year=year).values('date__month').annotate(total=Sum('amount'))
    data = [{'month': e['date__month'], 'amount': e['total']} for e in expenses]

    fig = px.bar(data, x='month', y='amount', title=f'Monthly Expenses for {year}')
    chart_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return render(request, 'analytics/monthly_expenses_in_year.html', {'chart_json': mark_safe(chart_json)})