from django.shortcuts import render,redirect
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import *



def index(request):
    products = Product.objects.all()
    return render(request, "index.html",{'products': products})

def shop(request):
    return render(request, "shop.html", {'username': request.user.username})

def shopdetail (request):
    return render(request,'shop-detail.html', {'username': request.user.username})



@login_required(login_url="login")
def cart(request):

    cartdata =  Cart.objects.filter(user=request.user)
    return render(request,'cart.html', {'username': request.user.username,'cartdata':cartdata})


@login_required(login_url="login")
def addtocart(request,id):

        productObject = Product.objects.get(id=id)
        Cart.objects.create(user=request.user,product=productObject,qty=1)
        return redirect("index")


def chackout(request):
    return render(request,"chackout.html", {'username': request.user.username})

def testimonial(request):
    return render(request,'testimonial.html', {'username': request.user.username})

def err(request):
    return render(request,'err.html', {'username': request.user.username})


def contact(request):
    return render(request,'contactt.html', {'username': request.user.username})

def logoutpage(request):
    logout(request)
    return render(request,"index.html")




def loginpage(request):
    if request.method == 'POST':
        data = request.POST
        username = data.get("username")
        password = data.get("password")

        if not User.objects.filter(username=username).exists():
            messages.info(request, "Invalid credentials1")
            return redirect("login")
        
        user = authenticate(username=username, password=password)
        if user is None:
            messages.info(request, "Invalid credentials")
            return redirect("login")
        else:
            login(request, user)
            return redirect("cart")
        
    return render(request,'login.html', {'username': request.user.username})

def regpage(request):
     
     if request.method=='POST':
          data = request.POST
          fname = data.get("fname")
          lname = data.get("lname")
          username = data.get("username")
          email = data.get("email")
          password = data.get("password")

          if User.objects.filter(username=username).exists():
            messages.info(request,"Username exists !!!")
            return redirect("reg")

          else:
            user =  User.objects.create(first_name=fname,last_name=lname,username=username,email=email)
            user.set_password(password)
            user.save()
            messages.info(request,"Registration successfully !!!")
            return redirect("reg")

     return render(request,"registration.html")