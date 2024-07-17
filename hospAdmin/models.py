from django.db import models

# Create your models here.
class Patientinfo(models.Model):
    date = models.DateField()
    address = models.CharField(max_length=100)
    id = models.CharField(max_length=100,primary_key=True)
    phone = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    marital_status = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=100)
    disease = models.CharField(max_length=100)
    blood_group = models.CharField(max_length=100)
    
class DoctorInfo(models.Model):
    joining_date = models.DateField()
    dept = models.CharField(max_length=100)
    id = models.CharField(max_length=100,primary_key=True)
    phone = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    user_name = models.CharField(max_length=100, default='default_user_name')
    age = models.IntegerField()
    marital_status = models.CharField(max_length=100)
    pwd = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    blood_group = models.CharField(max_length=100)

class ReceptionistInfo(models.Model):
    joining_date = models.DateField()
    id = models.CharField(max_length=100,primary_key=True)
    phone = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    user_name = models.CharField(max_length=100, default='default_user_name')
    age = models.IntegerField()
    marital_status = models.CharField(max_length=100)
    pwd = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    blood_group = models.CharField(max_length=100)
    
class AppointmentsInfo(models.Model):
    doc_id = models.CharField(max_length=100)
    patient_id = models.CharField(max_length=100)
    patient_name = models.CharField(max_length=100)
    disease = models.CharField(max_length=100)
    date = models.DateField()
    