# Generated by Django 3.1.7 on 2021-06-18 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mywebsite', '0002_auto_20210616_2238'),
    ]

    operations = [
        migrations.CreateModel(
            name='head_profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='0', max_length=25)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('email', models.CharField(default='0', max_length=20)),
                ('mobile', models.CharField(default='0', max_length=12)),
                ('address', models.CharField(default='0', max_length=50)),
                ('city', models.CharField(default='0', max_length=50)),
                ('state', models.CharField(default='0', max_length=50)),
                ('unicode', models.CharField(default='0', max_length=20)),
                ('country', models.CharField(default='0', max_length=20)),
                ('photo', models.FileField(default='0', upload_to='photo')),
            ],
        ),
    ]
