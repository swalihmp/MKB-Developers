from django.shortcuts import render
from adminp.models import Property,Photos,Amenities

# Create your views here.

# def custom_404(request, exception=None):
#     return render(request, '404.html')

def HomePage(request):
    completed = Property.objects.filter(status='Completed')
    ongoing = Property.objects.filter(status='Ongoing')
    context = {
        'completed':completed,
        'ongoing' : ongoing
    }
    return render(request,'index.html',context)