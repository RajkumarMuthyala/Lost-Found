from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login

# Create your views here.
def register(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if pass1 != pass2 :
            messages.warning(request, "Passwords are not matching")
            return redirect('register')
        try:
            if User.objects.get(username=uname):
                messages.warning(request, "Username already exist!")
                return redirect('register')
        except:
            pass

        my_user = User.objects.create_user(uname,'',pass1)
        my_user.save()
        messages.success(request, "Registration successful!! Please Login!")
        return redirect('/login')

    return render(request, 'users/register.html')

def login_user(request):

    if request.method == 'POST' :
        uname = request.POST.get('username')
        pswd = request.POST.get('password')
        user = authenticate(request, username=uname, password=pswd)
        if user is not None:
            login(request,user)
            return redirect('lost_and_found-home')
        else:
            messages.warning(request, "Username  or password is incorrect!!")
            return redirect('/login')

    return render(request, 'users/login.html')