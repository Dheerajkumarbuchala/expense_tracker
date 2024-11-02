from django.urls import path # type: ignore
from .views import signup_view, CustomLoginView

urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('login/', CustomLoginView.as_view(), name='login'),
]
