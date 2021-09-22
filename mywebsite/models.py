from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class profile(models.Model):
    fname= models.CharField(max_length=25, default='0')
    date_of_birth = models.DateField(null=True, blank=True)
    email = models.CharField(max_length=20, default='0')
    mobile= models.CharField(max_length=12, default='0')
    address = models.CharField(max_length=50, default='0')
    city= models.CharField(max_length=50, default='0')
    state = models.CharField(max_length=50, default='0')
    unicode= models.CharField(max_length=20, default='0')
    country = models.CharField(max_length=20, default='0')
    photo= models.FileField(upload_to='static/media/photo', default='0')


class doctor_profile(models.Model):
    us = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=20, default='0')
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=20, default='0')
    email = models.CharField(max_length=50, default='0')
    mobile_number = models.CharField(max_length=12, default='0')
    address = models.CharField(max_length=50, default='0')
    specialization = models.CharField(max_length=50, default='0')
    education = models.CharField(max_length=50, default='0')
    # password=models.CharField(max_length=20,default='0')
    doctors = models.FileField(upload_to='static/media/doctors', default='0')

class patient_profile(models.Model):
    us = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=20, default='0')
    date_of_birth = models.DateField(null=True, blank=True)
    email = models.CharField(max_length=50, default='0')
    mobile_number = models.CharField(max_length=12, default='0')
    address = models.CharField(max_length=50, default='0')
    patients = models.FileField(upload_to='static/media/patients', default='0')
    # password=models.CharField(max_length=20,default='0')

class appointment(models.Model):
    dr=models.ForeignKey(doctor_profile,on_delete=models.CASCADE)
    pt = models.ForeignKey(User, on_delete=models.CASCADE)
    doctor_name = models.CharField(max_length=20, default='0')
    patient_name = models.CharField(max_length=20, default='0')
    appt_date=models.DateField(null=True, blank=True)
    time_slot=models.CharField(null=True, blank=True,max_length=20)



