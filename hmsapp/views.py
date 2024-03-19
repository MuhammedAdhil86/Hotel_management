
from django.shortcuts import render,redirect
from .forms import signupform,signupform1,RoomForm
from .models import staff,customer,room
from django.contrib.auth import authenticate, login as log,logout
def home(request):
    return render(request,'index.html')

def register(request):
    form = signupform()
    if request.method == 'POST':
        form = signupform(request.POST,request.FILES)
        if form.is_valid():
             form.save()

    return render(request,"reg.html",{'form':form})



def employees_login(request):
    return render(request,'employees_login.html')

def userlog(request):
    if request.method=='POST':
        email = request.POST['email']
        password = request.POST['password']
        user= staff.objects.filter(email=email,password=password)
        if user :
            userdata=staff.objects.get(email=email)
            firstname=userdata.firstname
            email=userdata.email
            id=userdata.id
            
            username=userdata.username
           
            request.session['firstname']=firstname
            request.session['username']=username
            
            request.session['id']=id
          
            return redirect('staffprofile')
    return render(request,'employees_login.html') 

def detail_view(request):
        
    cr=staff.objects.all()
    return render(request,'detail_view.html',{'cr':cr})



def dashbord(request):
    return render(request,'dashbord.html')




def register_c(request):
    form = signupform1()
    if request.method == 'POST':
        form = signupform1(request.POST,request.FILES)
        if form.is_valid():
             form.save()
    return render(request,"reg.html",{'form':form})



def userlog_c(request):
    if request.method=='POST':
        email = request.POST['email']
        password = request.POST['password']
        user= customer.objects.filter(email=email,password=password)
        if user :
            userdata=customer.objects.get(email=email)
            firstname=userdata.firstname
            lastname=userdata.lastname
            email=userdata.email
            gender=userdata.gender
          
            username=userdata.username
            request.session['firstname']=firstname
            request.session['lastname']=lastname
            request.session['username']=username
            request.session['email']=email
            request.session['gender']=gender
           
            return redirect('customerprofile')
        
    return render(request,'customer_login.html') 

def detail_view_c(request):
        
    cr=customer.objects.all()
    return render(request,'detail_view_c.html',{'cr':cr})


def customerprofile(request):
    username=request.session['username']

    return render(request,'customer_profile.html',{'username':username})

def customerlogout(request):
    logout(request) 
    return redirect("customer_log")




def staffprofile(request):
    id=request.session['id']
    username=request.session['username']
    firstname=request.session['firstname']
    

    return render(request,'staff.html',{'username':username,'id':id,'firstname':firstname})


def stafflogout(request):
    logout(request) 
    return redirect("employees_login")



def update(request,pk):
    cr= staff.objects.get(id=pk)
    form=signupform(instance=cr)
    if request.method == 'POST':
        form=signupform(request.POST,instance=cr)
        if form.is_valid:
            form.save()
            return redirect('staffprofile')
    return render(request,'update.html',{'form':form,'cr':cr})

def delete(request,pk):
    cr=staff.objects.get(id = pk)
    cr.delete()
    return redirect('staffprofile')

def staff_update(request):
    return render(request,'update.html')



def roompage(request):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
             form.save()
             return redirect('staffprofile')
    return render(request,"roompage.html",{'form':form})



def roomdisplay(request):
        
    cr=room.objects.all()
    return render(request,'roomdisplay.html',{'cr':cr})
     


def about(request):
    return render(request,'about.html')


def contact(request):
    return render(request,'contact.html')











