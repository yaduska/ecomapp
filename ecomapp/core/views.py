from django.shortcuts import redirect, render
from item.models import Category,Item
from django.contrib.auth.admin import User
from .forms import SignupForm


# Create your views here.
def index(request):
    items=Item.objects.filter(is_sold=False)
    categories=Category.objects.all
    user_name=request.user.username
    return render(request,'core\index.html',{'items':items,'categories':categories,'username':user_name})

def contact(request):
    return render(request,'core\contact.html')

def about(request):
    return render(request,'core/about.html')

def signup(request):
    if request.method=='POST':
        signupForm=SignupForm(request.POST)
        if signupForm.is_valid:
            signupForm.save()
            return redirect('login/')
    else:
        signupForm=SignupForm()
    
    return render(request,'core/signup.html',{'signupForm':signupForm})
    
    
    
