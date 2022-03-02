# Generated by Django 3.2.5 on 2022-02-26 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DCInsideTitleModel',
            fields=[
                ('title', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('url', models.TextField(null=True)),
                ('add_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='DemandForecastModel',
            fields=[
                ('name', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('ipo_price', models.IntegerField(null=True)),
                ('ipo_value', models.IntegerField()),
                ('security', models.CharField(max_length=40, null=True)),
                ('demand_forecast_start', models.DateField(db_index=True)),
                ('demand_forecast_end', models.DateField(db_index=True)),
                ('hope_price_min', models.IntegerField()),
                ('hope_price_max', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='IPOScheduleModel',
            fields=[
                ('name', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('ipo_price', models.IntegerField(null=True)),
                ('security', models.CharField(max_length=40, null=True)),
                ('ipo_start', models.DateField(db_index=True)),
                ('ipo_end', models.DateField(db_index=True)),
                ('hope_price_min', models.IntegerField()),
                ('hope_price_max', models.IntegerField()),
                ('competition_rate', models.FloatField(null=True)),
            ],
        ),
    ]
