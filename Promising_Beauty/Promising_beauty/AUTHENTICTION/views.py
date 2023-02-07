from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth

# Create your views here.
def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password = request.POST['password']

        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            message='Invalid Credentials..'
            return redirect('login')
    else:
        return render(request,'CustRegLog.html')

def register(request):
    if request.method == 'POST':
        username=request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password1 = request.POST['password1']
        password2= request.POST['password2']
        email = request.POST['email']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                message='Username already Taken..'
            elif User.objects.filter(email=email).exists():
                message='Email already Taken..'
            else:
                user=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,password=password1,email=email)
                user.save();
                print('user created')
                return redirect('login')
        else:
            message='Password not Matching..'

    else:
        return render(request,'CustRegLog.html',{'msg':message})    

def logout(request):
    auth.logout(request)
    return redirect('/')