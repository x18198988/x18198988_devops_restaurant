from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import login as my_login, logout as my_logout, authenticate
from django.contrib.auth.models import User
from book.models import Table, Booking


def index(request):
    t=Table.objects.all()
    return render(request, 'index.html', {'t':t})

def about(request):
    return render(request, 'about.html')

def booking(request):
    t=Table.objects.all()
    return render(request, 'booking.html', {'t':t})

def contact(request):
    return render(request, 'contact.html')

def menu(request):
    return render(request, 'menu.html')

def service(request):
    return render(request, 'service.html')

def team(request):
    return render(request, 'team.html')

def testimonial(request):
    return render(request, 'testimonial.html')   

def login(request):
    return render(request, 'login.html')

def handle_login(request):
    if request.method == 'POST':
        uname = request.POST.get("uname")
        p1 = request.POST.get("p1")
        user = authenticate(username=uname, password=p1)
        if user is not None:
            my_login(request, user)

            # messages.success(request, "Logged in")
            return redirect('index')
        else:
            # messages.info(request,'invalid credentials')
            return redirect('login')  
    return redirect('index') 

def logout(request):
    my_logout(request)
    return redirect('index')

def signup(request):
    return render(request, 'signup.html')

def handle_signup(request):
    if request.method == 'POST':
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        uname = request.POST.get("uname")
        email = request.POST.get('email')
        p1 = request.POST.get("p1")
        p2 = request.POST.get("p2")
        
        if p1==p2:
        

            u = User.objects.create_user(username=uname, email=email, password=p1)
            u.first_name = fname
            u.last_name = lname

            u.save()
            # messages.success(request, "Your account has been created")
            print('success')
            return redirect("index")
    else:

        return HttpResponse("404 error") 

def handle_booking(request):
    if request.user.is_authenticated == 'POST':
        if request.method == 'POST':
            name=request.POST.get('name')
            
            date=request.POST.get('date')
            table=request.POST.get('table')
            sr=request.POST.get('sr')
            b=Booking(user_id=1, name=name, table_id=table, date_time=date, sr=sr)
            b.save()
            return redirect('index')
        else:

            return HttpResponse("404 error")
    else:

        return HttpResponse("404 error")        

def my_booking(request):
    if request.user.is_authenticated:
        b=Booking.objects.filter(user_id=request.user.pk)
        return render(request, 'my_bookings.html', {'b':b})
    else:   

        return HttpResponse("404 error") 

def edit_booking(request):
    if request.user.is_authenticated:
        id=request.POST.get('id')
        b=Booking.objects.get(pk=id)
        t=Table.objects.all()
        return render(request, 'edit_booking.html', {'b':b, 't':t})
    else:   

        return HttpResponse("404 error") 

def handle_edit_booking(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            id=request.POST.get('id')
            name=request.POST.get('name')
            
            date=request.POST.get('date')
            table=request.POST.get('table')
            sr=request.POST.get('sr')
            b=Booking.objects.get(pk=id)
            b.name=name
            b.date=date
            b.table_id=table
            b.sr=sr
            b.save()
            return redirect('my_booking')
        else:

            return HttpResponse("404 error")
    else:

        return HttpResponse("404 error") 

def delete_booking(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            id=request.POST.get('id')
            b=Booking.objects.get(pk=id)
            b.delete()
            return redirect('my_booking')
        else:

            return HttpResponse("404 error")
    else:

        return HttpResponse("404 error")    
