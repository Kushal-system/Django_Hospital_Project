# Generated by Django 3.1.7 on 2021-06-24 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mywebsite', '0017_auto_20210623_2008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='doctors',
            field=models.FileField(default='0', upload_to='static/media/doctors'),
        ),
        migrations.AlterField(
            model_name='doctor_profile',
            name='doctors',
            field=models.FileField(default='0', upload_to='static/media/doctors'),
        ),
        migrations.AlterField(
            model_name='patient_profile',
            name='patients',
            field=models.FileField(default='0', upload_to='static/media/patients'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.FileField(default='0', upload_to='static/media/photo'),
        ),
    ]
