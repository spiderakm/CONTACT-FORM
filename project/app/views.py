from django.shortcuts import render
from .models import Contact
from django.http import HttpResponse
# Create your views here.
def index(request):
    if request.method=="POST":
        contact=Contact()
        name=request.POST.get('name')
        email=request.POST.get('email')
        contact.name=name
        contact.email=email
        contact.save()
        return HttpResponse("<h1>Successfully Submitted</h1>")


    return render(request, 'index.html')
