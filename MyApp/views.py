from django.shortcuts import render , HttpResponse
from datetime import datetime
from MyApp.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'index.html')
    # return HttpResponse("this is home Page")

def menu(request):
    return render(request, 'menu.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        desc = request.POST.get('desc')
        contact = Contact(name=name,email=email,desc=desc,date=datetime.today())
        contact.save()
        messages.success(request, "Your message has been sent!s")
    return render(request, 'contact.html')