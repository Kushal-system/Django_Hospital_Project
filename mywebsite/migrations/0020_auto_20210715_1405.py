# Generated by Django 3.1.7 on 2021-07-15 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mywebsite', '0019_auto_20210712_1419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='time_slot',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
