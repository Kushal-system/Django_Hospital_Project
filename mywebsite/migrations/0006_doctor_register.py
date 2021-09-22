# Generated by Django 3.1.7 on 2021-06-20 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mywebsite', '0005_auto_20210618_1059'),
    ]

    operations = [
        migrations.CreateModel(
            name='doctor_register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor_name', models.CharField(default='0', max_length=20)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('gender', models.CharField(default='0', max_length=20)),
                ('email', models.CharField(default='0', max_length=50)),
                ('mobile_number', models.CharField(default='0', max_length=12)),
                ('address', models.CharField(default='0', max_length=50)),
                ('specialization', models.CharField(default='0', max_length=50)),
                ('education', models.CharField(default='0', max_length=50)),
                ('password', models.CharField(default='0', max_length=20)),
                ('img', models.FileField(default='0', upload_to='media/doctors')),
            ],
        ),
    ]
