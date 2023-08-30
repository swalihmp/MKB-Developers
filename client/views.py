from django.shortcuts import render
from adminp.models import Property,Photos,Amenities,Contact
from django.http import JsonResponse
import json
from django.contrib import messages,auth

# Create your views here.


def Projects(request):
    projects = Property.objects.all()
    context = {
        'projects':projects,
        'total': projects.count()
    }
    return render(request,'Property.html',context)


def Save_Data(request):
    # body = json.loads(request.body)
    
    # message = body['message']
    # name = body['name']
    # email = body['email']
    # number = body['number']
    if request.method == 'POST':
        message = request.POST['message']
        email = request.POST['email']
        name = request.POST['email']
        number = request.POST['number']
    
    
        data=Contact()
        
        data.message = message
        data.email = email
        data.name = name
        data.number = number
    
        data.save()
        
        messages.info(request, "Submited Successfully...!")
    
        return render(request,'contact.html')


def Project_details(request,id):
    details = Property.objects.get(id=id)
    photos = Photos.objects.filter(property=details)
    datas = Amenities.objects.filter(property=details)
    
    context = {
        'details':details,
        'photos': photos,
        'datas':datas
    }
    return render(request,'Property_details.html',context)

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')