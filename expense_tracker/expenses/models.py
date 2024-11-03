from django.db import models # type: ignore
from django.contrib.auth.models import User # type: ignore


CATEGORY_CHOICES = [
    ('food', 'Food'),
    ('transport', 'Transport'),
    ('entertainment', 'Entertainment'),
    ('utilities', 'Utilities'),
    # Add more categories as needed
]

# Create your models here.
class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    comments = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.date} - {self.category} - {self.amount}"