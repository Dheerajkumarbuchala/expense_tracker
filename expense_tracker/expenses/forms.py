# expenses/forms.py
from django import forms
from .models import Expense

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['date', 'amount', 'category', 'comments']
        widgets = {
            'date': forms.DateInput(attrs={'readonly': 'readonly'}),  # Keep the date readonly
        }