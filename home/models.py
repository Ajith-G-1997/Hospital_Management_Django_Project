from django.db import models

# Create your models here.
class Department(models.Model):
    dep_name=models.CharField(max_length=50)
    dep_description=models.TextField()
    
    def __str__(self):
        return self.dep_name


class Doctors(models.Model):
    doctor_name=models.CharField(max_length=50)
    doctor_special=models.CharField(max_length=50)
    department_name=models.ForeignKey(Department,on_delete=models.CASCADE)
    doctor_image=models.ImageField(upload_to='static/doctor-image')
    
    def __str__(self):
        return self.doctor_name
    
class Booking(models.Model):
    patient_id = models.AutoField(primary_key=True)
    patient_name = models.CharField(max_length=255)
    date=models.DateField()
    doctor_name = models.ForeignKey(Doctors, on_delete=models.CASCADE)
    department_name = models.ForeignKey(Department, on_delete=models.CASCADE)
    patient_number = models.IntegerField()
    
