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
    security = models.CharField(max_length=40, null=True)
    demand_forecast_start = models.DateField(db_index=True)
    demand_forecast_end = models.DateField(db_index=True)
    hope_price_min = models.IntegerField()
    hope_price_max = models.IntegerField()


class DemandForecastResultModel(models.Model):
    """
    DemandForecast에서
    hold_rate: 의무보유 확약 %
    institutional_competition_rate: 기관 경쟁률
    """
    company = models.CharField(max_length=20, primary_key=True)
    demand_forecast_date = models.DateField(null=True, db_index=True)
    ipo_price = models.IntegerField()
    ipo_value = models.IntegerField()
    institutional_competition_rate = models.FloatField()
    hold_rate = models.FloatField()
    security = models.CharField(max_length=40)
    hope_price_min = models.IntegerField()
    hope_price_max = models.IntegerField()


class IPOScheduleModel(models.Model):
    name = models.CharField(max_length=20, primary_key=True)
    ipo_price = models.IntegerField(null=True)
    security = models.CharField(max_length=40, null=True)
    ipo_start = models.DateField(db_index=True)
    ipo_end = models.DateField(db_index=True)
    hope_price_min = models.IntegerField()
    hope_price_max = models.IntegerField()
    competition_rate = models.FloatField(null=True)


class DCInsideTitleModel(models.Model):
    title = models.CharField(max_length=50, primary_key=True)
    url = models.TextField(null=True)
    add_date = models.DateTimeField(auto_now=True)


class DCInsideDetailModel(models.Model):
    title = models.ForeignKey(DCInsideTitleModel, on_delete=models.CASCADE)
    date_time = models.DateTimeField(db_index=True)
    content = models.TextField(null=True)


class NaverTrendSearchModel(models.Model):
    date = models.DateField()
    ratio = models.FloatField()
    company = models.CharField(max_length=25)

    class Meta:
        unique_together = (('date', 'company'),)
