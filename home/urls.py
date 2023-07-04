from django.urls import path
from . import views

urlpatterns = [
    path('',views.homepage,name='homepage'),
    path('about/',views.about,name='about'),
    path('booking/',views.booking_list,name='booking_list'),
    path('booking/create/',views.create_booking, name='create_booking'),
    path('doctors/',views.doctors,name='doctors'),
    path('doctor/<int:doctor_id>/', views.doctor_detail, name='doctor_detail'),

    path('department/',views.department,name='department'),
    path('contact/',views.contact,name='contact')
]
