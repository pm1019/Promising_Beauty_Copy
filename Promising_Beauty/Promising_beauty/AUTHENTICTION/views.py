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

        user=User.objects.create_user(password=password1,email=email,first_name=first_name,last_name=last_name,username=username)
        user.save();
        print('user created')
        return redirect('/')

    else:
        return render(request,'CustRegLog.html')    