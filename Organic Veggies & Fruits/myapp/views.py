from django.shortcuts import render,redirect
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import *
import random
from django.conf import settings
from django.core.mail import send_mail



def index(request):
    products = Product.objects.all()
    return render(request, "index.html",{'products': products,'username': request.user.username})

def shop(request):
    return render(request, "shop.html", {'username': request.user.username})

def shopdetail (request):
    return render(request,'shop-detail.html', {'username': request.user.username})



@login_required(login_url="login")
def cart(request):
    cartdata = Cart.objects.filter(user=request.user)

    subtotal = 0
    for item in cartdata:
        subtotal += item.product.price * item.qty
 
    shipping_cost = 50
    
    final_bill = subtotal + shipping_cost
    
    return render(request, 'cart.html', {'username': request.user.username,'cartdata': cartdata,'subtotal': subtotal,'shipping_cost': shipping_cost,'final_bill': final_bill})





@login_required(login_url="login")
def addtocart(request, id):
    product_object = Product.objects.get(id=id)
    user_cart = Cart.objects.filter(user=request.user, product=product_object).first()
    print(product_object)
    print(request.user)
    print(product_object.id)
    if user_cart:
        user_cart.qty += 1
        user_cart.save()
    else:
        Cart.objects.create(user=request.user, product=product_object, qty=1)
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
          
          request.session['fname']=fname
          request.session['lname']=lname
          request.session['username']=username
          request.session['email']=email
          request.session['password']=password

          if User.objects.filter(username=username).exists():
            messages.info(request,"Username exists !!!")
            return redirect("reg")

          else:
            otp = random.randint(1000, 9999)
            request.session['otp'] = otp  # Store OTP in session
            
            subject = 'Welcome to GFG world'
            message = f'Hi {username}, thank you for registering on GeeksforGeeks. Your OTP is {otp}'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email]
        
            send_mail(subject, message, email_from, recipient_list)
            return redirect('otp_verification')

     return render(request,"registration.html")


def otp_verification(request):
    
    if request.method == "POST":
        entered_otp = request.POST.get('entered_otp')
        stored_otp = request.session.get('otp')
        if entered_otp == str(stored_otp):
            email = request.session.get('email')
            fname = request.session.get('fname')
            lname = request.session.get('lname')
            username = request.session.get('username')
            password = request.session.get('password')
            user =  User.objects.create(first_name=fname,last_name=lname,username=username,email=email)
            user.set_password(password)
            user.save()  
            return redirect('index')
        else:
            return redirect("otp_verification")
        
    email = request.session.get('email')
    otp = request.session.get('otp')
    return render(request, 'otp.html', {'email': email, 'otp': otp})


def delete(request,id):
    cartdata = Cart.objects.get(id=id)
    cartdata.delete()
    return redirect("cart")


def plus(request,id):
    cartdata = Cart.objects.get(id=id)
    cartdata.qty += 1
    cartdata.save()
    return redirect("cart")


def minus(request,id):
    cartdata = Cart.objects.get(id=id)
    cartdata.qty -= 1
    cartdata.save()
    return redirect("cart")