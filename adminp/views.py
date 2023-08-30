from django.shortcuts import render,redirect
import json
from django.http import HttpResponse,JsonResponse
from .models import Property,Photos,Amenities,Contact
import os
from django.contrib import messages,auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout

# Create your views here.


# def AddProperty(request):
#     return render(request,'admin/addproperty.html')

def Loginp(request):
    if 'username' in request.session:
        if request.user.is_authenticated:
            return redirect('homepage')
        else:
            return render(request,'admin/login.html')
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request,username=username,password=password)
        
        if user is not None:
            login(request,user)
            request.session['username'] = username
            return redirect('homepage')
        else:
            messages.info(request, "Invalid Credentials...!")
            return render(request,'admin/login.html')
    else:
        return render(request,'admin/login.html')
    

@login_required(login_url = 'login')
def AddMore(request):
    propertys = Property.objects.all()
    context={
        'property':propertys
    }
    return render(request,'admin/adddetails.html',context)

@login_required(login_url = 'login')
def HomePage(request):
    propertys = Property.objects.all()
    completed = Property.objects.filter(status='Completed')
    ongoing = Property.objects.filter(status='Ongoing')
    planning = Property.objects.filter(status='Planning')
    context={
        'property':propertys,
        'completed' : completed.count(),
        'ongoing' : ongoing.count(),
        'planning' : planning.count()
    }
    return render(request,'admin/adminhome.html',context)


@login_required(login_url = 'login')
def Enquiry(request):
    enquires = Contact.objects.all()
    print(enquires)
    context = {
        'enquiries':enquires
    }
    return render(request,'admin/enquiries.html',context)



@login_required(login_url = 'login')
def Mark(request,id):
    data = Contact.objects.get(id=id)
    data.mark = True
    data.save()
    return redirect('enquiries') 




@login_required(login_url = 'login')
def Addimage(request):
    if request.method == 'POST':
        pname = request.POST['pname']
        img = request.FILES['img']
        
        property = Property.objects.get(pname=pname)
        
        Photos.objects.create(property=property,image=img)
        
        propertys = Property.objects.all()
        context={
            'property':propertys
        }
        
        return render(request,'admin/adddetails.html',context)
    



@login_required(login_url = 'login')    
def Adddata(request):
    if request.method == 'POST':
        pname = request.POST['pname']
        data = request.POST['data']
        
        property = Property.objects.get(pname=pname)
        
        Amenities.objects.create(property=property,data=data)
        
        propertys = Property.objects.all()
        context={
            'property':propertys
        }
        
        return render(request,'admin/adddetails.html',context)



@login_required(login_url = 'login')
def AddProperty(request):
    if request.method == 'POST':
        pname = request.POST['pname']
        plocation = request.POST['plocation']
        pdimension = request.POST['pdimension']
        status = request.POST['status']
        coverimage = request.FILES['coverimage']
        
        image1 = request.FILES['image1']
        image2 = request.FILES['image2']
        image3 = request.FILES['image3']
        image4 = request.FILES['image4']
        image5 = request.FILES['image5']
        
        data1 = request.POST['data1']
        data2 = request.POST['data2']
        data3 = request.POST['data3']
        data4 = request.POST['data4']
        
        
        list1 = [image1,image2,image3,image4,image5]
        list2 = [data1,data2,data3,data4]

        
        Property.objects.create(pname=pname,plocation=plocation,pdimension=pdimension,status=status,coverimage=coverimage)
        
        prop = Property.objects.last()
        
        for images in list1:  
            photo = Photos(property=prop, image=images)
            photo.save()
            
        for datas in list2:  
            data = Amenities(property=prop, data=datas)
            data.save()
        
        return render(request,'admin/addproperty.html')
    else:
        return render(request,'admin/addproperty.html')
    
    
    



@login_required(login_url = 'login')    
def change(request,id,action):
    
    property = Property.objects.get(id=id)
    print(property)
    
    if action=='Ongoing':
        property.status="Ongoing"
        property.save()
    elif action =='Completed':
        property.status="Completed"
        property.save()

    return redirect('homepage')




@login_required(login_url = 'login')
def Single(request,id):
    if request.method=='POST':
        prop = Property.objects.get(id=id)
        if not request.FILES.get('coverimage'):
            ex1 = Property.objects.filter(id=id).update(
                pname = request.POST['pname'],
                plocation = request.POST['plocation'],
                pdimension = request.POST['pdimension'],
            )
        else:
            os.remove(prop.coverimage.path)
            prop.coverimage = request.FILES['coverimage']
            prop.save()
            ex1 = Property.objects.filter(id=id).update(
                pname = request.POST['pname'],
                plocation = request.POST['plocation'],
                pdimension = request.POST['pdimension']
            )
        return redirect('homepage')
    else:
        property = Property.objects.get(id=id)
        
        amenities = Amenities.objects.filter(property=property)
        photots = Photos.objects.filter(property=property)
        
        context ={
            'property':property,
            'amenities':amenities,
            'property_id':id,
            'photos':photots
        }
        return render(request,'admin/singleproperty.html',context)




@login_required(login_url = 'login')
def EditData(request):
    if request.method == 'POST':
        for key, value in request.POST.items():
            if key.startswith('data_'):
                amenity_id = key.replace('data_', '')
                amenity_data = value
                Amenities.objects.filter(id=amenity_id).update(data=amenity_data)
    return redirect('homepage')




@login_required(login_url = 'login')
def RemoveAmenti(request,id,id1):
    print(id,id1)
    
    datas = Amenities.objects.get(id=id)
    datas.delete()
    
    property = Property.objects.get(id=id)
        
    amenities = Amenities.objects.filter(property=property)
    photots = Photos.objects.filter(property=property)
    
    context ={
        'property':property,
        'amenities':amenities,
        'property_id':id,
        'photos':photots
    }
    return render(request,'admin/singleproperty.html',context)



@login_required(login_url = 'login')
def RemoveImage(request,id,id1):
    print(id,id1)
    
    datas = Photos.objects.get(id=id)
    datas.delete()
    
    
    property = Property.objects.get(id=id)
        
    amenities = Amenities.objects.filter(property=property)
    photots = Photos.objects.filter(property=property)
    
    context ={
        'property':property,
        'amenities':amenities,
        'property_id':id,
        'photos':photots
    }
    return render(request,'admin/singleproperty.html',context)



@login_required(login_url = 'login')
def logout_p(request):
    if 'username' in request.session:
        request.session.flush()
        logout(request)
        return redirect('login')