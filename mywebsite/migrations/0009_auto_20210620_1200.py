# Generated by Django 3.1.7 on 2021-06-20 06:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mywebsite', '0008_auto_20210620_1156'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doctor_register',
            old_name='dname',
            new_name='name',
        ),
    ]
