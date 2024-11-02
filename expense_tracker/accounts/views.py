from django.shortcuts import render # type: ignore
from django.shortcuts import render, redirect # type: ignore
from django.contrib.auth import login # type: ignore
from django.contrib.auth.views import LoginView # type: ignore
from .forms import SignupForm

# Create your views here.

def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log the user in after signup
            return redirect('calendar_view')  # Replace with the name of your calendar view
    else:
        form = SignupForm()
    return render(request, 'accounts/signup.html', {'form': form})


class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'