# Generated by Django 3.1.7 on 2021-06-20 06:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mywebsite', '0006_doctor_register'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doctor_register',
            old_name='img',
            new_name='doctors',
        ),
    ]
