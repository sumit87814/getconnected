from django.shortcuts import render,HttpResponse
from app.models import Contact
from django.contrib import messages

# Create your views here.
def index(requests):
    # return HttpResponse("this is homepage")
    return render(requests,'index.html')

def about(requests):
    return HttpResponse("this is about page")

def services(requests):
    return HttpResponse("this is services page")

def contact(requests):
    if requests.method =="POST":
        email = requests.POST.get("email")
        password = requests.POST.get("password")
        contact = Contact(email=email, password=password)
        contact.save()
        messages.success(requests, 'submitted.')

    # return HttpResponse("this is contact page")
    return render(requests, 'contact.html' )
