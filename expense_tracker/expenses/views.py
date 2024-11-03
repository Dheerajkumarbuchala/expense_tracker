from django.shortcuts import render, redirect # type: ignore
from django.contrib.auth.decorators import login_required # type: ignore
from .forms import ExpenseForm
from django.db.models import Sum
from .models import Expense
from django.http import JsonResponse
import json
from django.utils.safestring import mark_safe
from django.views.decorators.cache import cache_control

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
def add_expense_view(request, date):
    expenses = Expense.objects.filter(user=request.user, date=date)
    daily_total = expenses.aggregate(Sum('amount'))['amount__sum'] or 0  # Calculate total or 0 if none

    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user
            expense.save()
            # If AJAX request, return JSON response
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
            return redirect('calendar_view')
    else:
        form = ExpenseForm(initial={'date': date})  # Pre-fill the date field for GET requests

    context = {
        'form': form,
        'selected_date': date,
        'expenses': expenses,
        'daily_total': daily_total,
    }
    return render(request, 'expenses/add_expense.html', context)