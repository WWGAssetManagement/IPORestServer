from django.db import models


# Create your models here.

class DemandForecastModel(models.Model):
    """
    name: 종목명
    demand_forecast_start ~ end: 수요 예측일
    hope_min ~ max: 희망 공모가
    security: 주관사
    ipo_value: 공모금액(백만)
    """
    name = models.CharField(max_length=20, primary_key=True)
    ipo_price = models.IntegerField(null=True)
    ipo_value = models.IntegerField()
    security = models.CharField(max_length=20)
    demand_forecast_start = models.DateField(db_index=True)
    demand_forecast_end = models.DateField(db_index=True)
    hope_price_min = models.IntegerField()
    hope_price_max = models.IntegerField()
