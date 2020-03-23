from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Tutorial
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate

def home(request):
    return render(request=request,
    template_name="TINY/home.html",
    context={"tutorials": Tutorial.objects.all})

def register(request):

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect("TINY:home")
        else:
            for msg in form.error_messages:
                print(form.error_messages[msg])
    form = UserCreationForm
    return render(request,
                  "TINY/register.html",
                  context={"form":form}) # must be tha same name as the one in register.html
        
def logout_(request):
    logout(request)
    messages.info(request, "logged out successfully!")
    return redirect("TINY:login")

"""def login_(request):
           form = AuthenticationForm()
    return render(request,
                  "TINY/login.html",
                  context={"form":form}) # must be tha same name as the one in register.html
  """