from django.shortcuts import render, redirect
from django.contrib import messages

from django.contrib.auth import authenticate, login, logout

from .forms import MyUserCreationForm

from .models import User





def signin(request):
# CHECK IF USER IS LOGGED IN
    if request.user.is_authenticated:
        return redirect('/')

    # GET USERNAME
    if request.method == "POST":
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

    # CHECK IF USER EXISTS IN DB
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'user does not exist!')

    # IF USER EXIST CHECK IF CREDENTIALS MATCH AN EXISTING ONE IN DB  
        user = authenticate(request, username=username, password=password)

    # IF CREDENTIALS MATCH THEN LOGIN USER TO HOMEPAGE
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'username OR password incorrect!')
    return render(request, 'users/login.html')


def signup(request):
    form = MyUserCreationForm()

    if request.method == "POST":
        form = MyUserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()

            if user is not None:
                login(request, user)
                return redirect('/')
    else:
        form = MyUserCreationForm()
    context = {'form':form}
    return render(request, 'users/signup.html', context)


def signout(request):
    logout(request)
    return redirect('/')