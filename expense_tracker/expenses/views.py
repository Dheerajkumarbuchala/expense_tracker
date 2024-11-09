from django.shortcuts import render, redirect # type: ignore
from django.contrib.auth.decorators import login_required # type: ignore
from .forms import ExpenseForm
from django.db.models import Sum
from .models import Expense
from django.http import JsonResponse
import json
from django.utils.safestring import mark_safe
from django.views.decorators.cache import cache_control
from datetime import date, datetime

# Create your views here.
@login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def calendar_view(request):
    # Retrieve total expenses per day for the logged-in user
    daily_totals = (
        Expense.objects.filter(user=request.user)
        .values('date')
        .annotate(total=Sum('amount'))
    )

    # Format the totals for the calendar in JSON format
    events = [{'title': f"${total['total']}", 'start': total['date'].strftime('%Y-%m-%d')} for total in daily_totals]
    events_json = json.dumps(events)  # Convert to JSON format
    context = {'events_json': mark_safe(events_json)}  # Mark JSON as safe for template use

    return render(request, 'expenses/calendar.html', context)


@login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def add_expense_view(request, date_str=None):
    # Parse the date from the URL if provided, otherwise use today's date
    selected_date = datetime.strptime(date_str, '%Y-%m-%d').date() if date_str else date.today()

    # Get expenses and calculate the daily total for the selected date
    expenses = Expense.objects.filter(user=request.user, date=selected_date)
    daily_total = expenses.aggregate(Sum('amount'))['amount__sum'] or 0

    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user
            expense.date = selected_date  # Set the selected date for the expense
            expense.save()
            # If AJAX request, return JSON response with updated totals
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({
                    'status': 'success',
                    'daily_total': daily_total + expense.amount,
                    'new_expense': {
                        'category': expense.category,
                        'amount': expense.amount,
                        'comments': expense.comments or ""
                    }
                })
            return redirect('main_visualization')  # Redirect to dashboard after adding expense
    else:
        form = ExpenseForm(initial={'date': selected_date})  # Pre-fill the date field for GET requests

    context = {
        'form': form,
        'selected_date': selected_date,
        'expenses': expenses,
        'daily_total': daily_total,
    }
    return render(request, 'expenses/add_expense.html', context)