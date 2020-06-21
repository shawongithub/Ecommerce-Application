from django.shortcuts import render, HttpResponseRedirect, redirect
from django.urls import reverse
from django.http import HttpResponse

# Create your views here.
# Authentication
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate

#models and forms

from App_Login.models import Profile
from App_Login.forms import ProfileForm, SignUpForm

from django.contrib import messages

def sign_up(request):
    form=SignUpForm()
    if request.method == 'POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Account created successfully")
            return HttpResponse('signup successfully')
    return render(request,'App_Login/sign_up.html',context={'form':form})

def login__user(request):
    form=AuthenticationForm()
    if request.method=='POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect(reverse('App_Shop:home'))
    return render(request,'App_Login/login.html',context={'form':form})

@login_required
def logout_user(request):
    logout(request)
    messages.warning(request,"you are logged out successfully")
    return HttpResponseRedirect(reverse('App_Shop:home'))

@login_required
def user_profile(request):
    profile=Profile.objects.get(user=request.user)
    form=ProfileForm(instance=profile)

    if request.method=='POST':
        form=ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request,"your profile is changed successfully")
            form=ProfileForm(instance=profile)
            return redirect("App_Payment:checkout")

    
    
    return render(request,'App_Login/change_profile.html',context={'form':form})
