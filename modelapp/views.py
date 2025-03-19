from idlelib.query import Query

from django.shortcuts import render,redirect
from . models import Students

# Create your views here
def index(request):
    users = Students.objects.all()
    return render(request,'index.html',{'users':users})
def addstudent(request):
    if request.method == "POST":
        firstname = request.POST['firstname']
        last_name = request.POST['last_name']
        email = request.POST['email']
        gender = request.POST['gender']
        date_of_birth = request.POST['date_of_birth']
        query=Students(firstname=firstname,last_name=last_name,email=email, gender=gender,date_of_birth=date_of_birth)
        query.save()
        return redirect('/')

    return render(request,'addusers.html')


