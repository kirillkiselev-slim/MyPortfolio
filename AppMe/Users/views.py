from .forms import NewUserForm
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate  # add this
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm


def homepage(request):
    return render(request, 'index.html')


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password1 = form.cleaned_data.get("password1")
            password2 = form.cleaned_data.get('password2')
            if password1 != password2:
                form.add_error('password1', 'Passwords do not match')
            elif User.objects.filter(username=username).exists():
                form.add_error('username', 'Username is taken!')
            authenticate(username=username, password=password1)
            user = form.save()
            login(request, user)
            return redirect('../maps')

    else:
        form = NewUserForm()
    return render(request=request, template_name="users/register.html", context={"form": form})


def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')

        messages.error(request,'Incorrect username or password!')

    return render(request=request, template_name="users/login.html", context={})


@login_required()
def logoutUser(request):
    logout(request)
    return redirect('/')

# Create your views here.
