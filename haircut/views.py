from django.shortcuts import render
from . models import Appointment


def home_page(request): 

    if request.method == 'POST':
        customer_name = request.POST.get('customer_name')   
        date =request.POST.get("date") 
        time =request.POST.get("time") 
        barber =request.POST.get("barber") 

        # Save Information in database
        Appointment.objects.create(
            time=time,
        	date=date,
        	customer_name=customer_name,
        	barber=barber
        )

        # Pass ALL Database records of haircuts to our template; 
        appointments = Appointment.objects.all()
        context = {'appointments': appointments}
    
        return render(request, 'haircut/home_page.html', context )
    appointments = Appointment.objects.all()
    context = {'appointments': appointments}
    return render(request, 'haircut/home_page.html', context) 


