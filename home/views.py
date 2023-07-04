from django.shortcuts import render,get_object_or_404,redirect
from .models import Department,Doctors,Booking
from .forms import BookingForm

# Create your views here.

def homepage(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def booking_list(request):
    booking=Booking.objects.all()
    return render(request,'booking_list.html',{'booking':booking})

def create_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('booking_list') 
    else:
        form = BookingForm()
    
    context = {'form': form}
    return render(request, 'booking_form.html', context)


def doctors(request):
    doctors=Doctors.objects.all()
    return render(request,'doctors.html',{'doctors': doctors})

def doctor_detail(request, doctor_id):
    doctor = get_object_or_404(Doctors, id=doctor_id)
    return render(request, 'doctor_detail.html', {'doctor': doctor})

def contact(request):
    return render(request,'contact.html')

def department(request):
    dept = Department.objects.all()
    return render(request, 'department.html', {'dept': dept})