from django.contrib import admin
from .models import Department,Doctors,Booking

# Register your models here.

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['dep_name', 'dep_description']

admin.site.register(Department,DepartmentAdmin)

class DoctorsAdmin(admin.ModelAdmin):
    list_display = ['doctor_name', 'doctor_special','department_name','doctor_image']

admin.site.register(Doctors,DoctorsAdmin)

class BookingAdmin(admin.ModelAdmin):
    list_display = ['patient_name', 'date','doctor_name','department_name','patient_number']

admin.site.register(Booking,BookingAdmin)