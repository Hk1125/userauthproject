from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from uapp.forms import RegisterForm
from django.http import HttpResponseRedirect

# Create your views here.

def homeview(request):
	return render(request,'uapp/home.html')

@login_required
def javaexamsview(request):
	return render(request,'uapp/javaexams.html')

def pythonexamsview(request):
	return render(request,'uapp/pythonexams.html')

def thanksview(request):
	return render(request,'uapp/thanks.html')

def logout_view(request):
    logout(request)
    return redirect('/thanks')

def signup_view(request):
	form=RegisterForm()
	if request.method=="POST":
		form=RegisterForm(request.POST)
		user=form.save() #create user object
		user.set_password(user.password) #use set_password predefined
		user.save() #save user
		return HttpResponseRedirect('/accounts/login')
	return render(request,'uapp/register.html',{'form':form})

