from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth import authenticate, login as signin, logout as signsout
from . import forms
from django.contrib.auth.forms import SetPasswordForm
# from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.urls import reverse
from .models import Classroom, BdOSN, MasLAB
import datetime

# Create your views here.


def home(request):
    data = forms.LoginForm()
    if request.user.is_authenticated:
        return HttpResponseRedirect("profile")
    else:
        if request.method == "POST":
            data = forms.LoginForm(request=request, data=request.POST)
            if data.is_valid():
                username = data.cleaned_data["username"]
                password = data.cleaned_data["password"]
                user = authenticate(username = username, password = password)
                if user is not None:
                    signin(request, user)
                    messages.success(request, "Login Successfull")
                    return HttpResponseRedirect("profile")
            else:
                messages.warning(request, "Invallied Username or Password")     
        else:
            return render(request, "html/home.html", {"form": data})
    return render(request, "html/home.html", {"form": data})
    

def profile(request):
    if request.user.is_authenticated:
        classroom = {
            
            "title": "Class Room",
            "text": "With the capacity of 40 peoples it is a class room you can book. Projector and aditional chairs will be provided if required.",
            "url": reverse("classroom")
        }
        maslab = {
            
            "title": "MasLAB",
            "text": "This is a place with the educational LAB facility. 15 Students can perform basic Lab test and learn from BdOSN researchers.",
            "url": reverse("maslab")
        }
        bdosn = {
            
            "title": "BdOSN",
            "text": "This place is the inner place of BdOSN. Only office staff meeting can be held here. The capacity of the peoples are around 20.",
            "url": reverse("bdosn")
        }
        data = {
            "classroom":classroom,
            "maslab":maslab,
            "bdosn":bdosn
        }
        return render(request, "html/profile.html", {"rooms":data})
    else:
        return HttpResponseRedirect("/bookings/")

# def signup(request):
#     return render(request, "/html/signup.html")


# def signin(request):
#     return render(request, "/html/signin.html")


def signout(request):
    
    if request.user.is_authenticated:
        signsout(request)
        messages.warning(request, "You Have Logged Out")
        return HttpResponseRedirect("/bookings/")
    else:
        return HttpResponseRedirect("profile")



 



def classroom(request):
    form = forms.BookingForm()
    if request.user.is_authenticated:
        if request.method == "POST":
            fm = forms.BookingForm(request.POST)
            if fm.is_valid():
                title = fm.cleaned_data["title"]
                email = fm.cleaned_data["email"]
                phone = fm.cleaned_data["phone"]
                date = fm.cleaned_data["date"]
                start_time = fm.cleaned_data["start_time"]
                end_time = fm.cleaned_data["end_time"]
                booked_by = request.user.first_name + " " + request.user.last_name
                current_date = datetime.date.today()
                if current_date >= date:
                    messages.warning(request, "Date is over already")
                    return HttpResponseRedirect("classroom")
                else:
                    booking_data = Classroom(title=title, booked_by=booked_by, email=email, phone=phone, date=date, start_time=start_time, end_time=end_time)
                    booking_data.save()
                    messages.success(request, "Room Booked Successfully")
                    return HttpResponseRedirect("classroom")
        else:
            current_date = datetime.date.today() 
            table = Classroom.objects.all()
            for date in table:
                if current_date < date.date:
                    print(date.title)
                else:
                    Classroom.objects.filter(pk = date.id).delete()
            return render(request, "html/booking.html", {"data": form,"rooms":"ClassRoom", "bookings":table})
    return render(request, "html/booking.html", {"data": form,"rooms":"ClassRoom", "bookings":table})


def bdosn(request):
    form = forms.BookingForm()
    if request.user.is_authenticated:
        if request.method == "POST":
            fm = forms.BookingForm(request.POST)
            if fm.is_valid():
                title = fm.cleaned_data["title"]
                email = fm.cleaned_data["email"]
                phone = fm.cleaned_data["phone"]
                date = fm.cleaned_data["date"]
                start_time = fm.cleaned_data["start_time"]
                end_time = fm.cleaned_data["end_time"]
                booked_by = request.user.first_name + " " + request.user.last_name
                current_date = datetime.date.today()
                if current_date >= date:
                    messages.warning(request, "Date is over already")
                    return HttpResponseRedirect("maslab")
                else:
                    booking_data = BdOSN(title=title, booked_by=booked_by, email=email, phone=phone, date=date, start_time=start_time, end_time=end_time)
                    booking_data.save()
                    messages.success(request, "Room Booked Successfully")
                    return HttpResponseRedirect("bdosn")
        else:
            current_date = datetime.date.today() 
            table = BdOSN.objects.all()
            for date in table:
                if current_date < date.date:
                    print(date.title)
                else:
                    BdOSN.objects.filter(pk = date.id).delete()
            return render(request, "html/booking.html", {"data": form,"rooms":"BdOSN", "bookings":table})
    return render(request, "html/booking.html", {"data": form,"rooms":"BdOSN", "bookings":table})


def maslab(request):
    form = forms.BookingForm()
    if request.user.is_authenticated:
        if request.method == "POST":
            fm = forms.BookingForm(request.POST)
            
            if fm.is_valid():
                title = fm.cleaned_data["title"]
                email = fm.cleaned_data["email"]
                phone = fm.cleaned_data["phone"]
                date = fm.cleaned_data["date"]
                start_time = fm.cleaned_data["start_time"]
                end_time = fm.cleaned_data["end_time"]
                booked_by = request.user.first_name +" " + request.user.last_name
                current_date = datetime.date.today()
                if current_date >= date:
                    messages.warning(request, "Date is over already")
                    return HttpResponseRedirect("maslab")
                else:
                    booking_data = MasLAB(title=title, booked_by=booked_by, email=email, phone=phone, date=date, start_time=start_time, end_time=end_time)
                    booking_data.save()
                    messages.success(request, "Room Booked Successfully")
                    return HttpResponseRedirect("maslab")
        else:
            table = MasLAB.objects.all()
            for date in table:
                if current_date < date.date:
                    print(date.title)
                else:
                    MasLAB.objects.filter(pk = date.id).delete()
            return render(request, "html/booking.html", {"data": form,"rooms":"MasLAB", "bookings":table})
    return render(request, "html/booking.html", {"data": form,"rooms":"MasLAB", "bookings":table})


