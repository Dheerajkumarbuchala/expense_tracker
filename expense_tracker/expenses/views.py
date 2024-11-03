from django.shortcuts import render # type: ignore
from django.contrib.auth.decorators import login_required # type: ignore

# Create your views here.
@login_required
def calendar_view(request):
    return render(request, 'expenses/calendar.html')

@login_required
def add_expense_view(request, date):
    context = {'selected_date': date}
    return render(request, 'expenses/add_expense.html', context)