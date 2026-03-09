from django.shortcuts import render
from hospital.models import Doctor, Department, Service
from formalar.models import Appointment, Contact
from .models import About, FAQ, Gallery
# Create your views here.
def doctor_view(request):
    doctors = Doctor.objects.all()
    departments = Department.objects.all()
    services = Service.objects.all()
    contact = Contact.objects.all()
    appointment = Appointment.objects.all()
    about=About.objects.last()
    gallery=Gallery.objects.all()
    faq=FAQ.objects.all()
    doctors_count = doctors.count()
    depts_count = departments.count()
    research_labs = 12
    awards = 15
    context = {
        'doctors': doctors,
        'departments': departments,
        'services': services,
        'contact': contact,
        'appointment': appointment,
        'about': about,
        'gallery': gallery,
        'faq': faq,
        'd_count': doctors_count,
        'dep_count': depts_count,
        'lab_count': research_labs,
        'award_count': awards,
    }
    return render(request, 'index.html', context)

