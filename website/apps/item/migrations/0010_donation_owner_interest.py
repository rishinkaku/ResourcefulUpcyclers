# Generated by Django 2.0.1 on 2018-02-17 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0009_auto_20180217_0437'),
    ]

    operations = [
        migrations.AddField(
            model_name='donation',
            name='owner_interest',
            field=models.BooleanField(default=False),
        ),
    ]
