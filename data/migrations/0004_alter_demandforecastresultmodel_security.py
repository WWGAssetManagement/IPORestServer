# Generated by Django 3.2.5 on 2022-03-08 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0003_demandforecastresultmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='demandforecastresultmodel',
            name='security',
            field=models.CharField(max_length=40),
        ),
    ]
