from rest_framework import serializers
from .models import DemandForecastModel


class DemandForecastSerializer(serializers.ModelSerializer):
    class Meta:
        model = DemandForecastModel
        fields = ('name',
                  'ipo_price',
                  'ipo_value',
                  'security',
                  'demand_forecast_start',
                  'demand_forecast_end',
                  'hope_price_min',
                  'hope_price_max',
                  )


