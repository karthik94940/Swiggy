# Generated by Django 3.0 on 2020-04-27 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0003_auto_20200427_0913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurantregistrationmodel',
            name='restaurant_otp',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='restaurantregistrationmodel',
            name='restaurant_password',
            field=models.CharField(max_length=16),
        ),
    ]