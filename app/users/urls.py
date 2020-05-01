from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path('create/', views.CreateView.as_view(), name='create'),
    path('token/', views.TokenView.as_view(), name='token'),
    path('me/', views.UpdateViwe.as_view(), name='me')
]
