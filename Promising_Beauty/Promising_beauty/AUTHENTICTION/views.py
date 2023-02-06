from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth

# Create your views here.
def login(request):
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
            user=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,password1=password1,password2=password2,email=email)
            user.save();
            print('user created')
            return redirect('/')
        elif User.objects.filter(username=username):
            message='Username already Taken..'
        else:
            message='Password not Matching..'

    else:
        return render(request,'CustRegLog.html',{'msg':message})    