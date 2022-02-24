from django.urls import path
from .views import demand_forecast

urlpatterns = [
    path('demand/forecast', demand_forecast)
]
