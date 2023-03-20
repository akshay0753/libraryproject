from django.shortcuts import render ,redirect

# Create your views here.
from .models import *
from django.http import HttpRequest,HttpResponse
from django.contrib.auth import login,authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

def homepage(request):
    print("kkkkkkk")
    if request.method == "POST":
        print(request.POST.get("bid"),788888888)
        bname = request.POST.get("bname")
        bprice = request.POST.get("bprice")
        bqty = request.POST.get("bqty")
        bpub = request.POST.get("bpub")
        bid = request.POST.get("bid")
        print(bid,"@@@@@@@@@@@@@@")
        if not bid:
            if bpub == "yes":
                bpub =True
            else:
                bpub = False
            obj = Book(name=bname, price=float(bprice), qty=int(bqty), is_published=bpub)
            obj.save()
            # return HttpResponse ("added")
            return render (request,"show_book.html",{"all_book":Book.objects.all()})        
            
        else:
            print(bid)
            obj = Book.objects.get(pk=bid)
            obj.name = bname
            obj.price = bprice
            obj.qty = bqty
            obj.is_published = bpub
            if bpub == "yes":
                    bpub =True
            else:
                bpub = False
            obj.save()
            # return HttpResponse("updated")
            return redirect ("show-book")        
    return render (request,"home.html")      
                
def book_update(request,pk):
    book =Book.objects.get(id=pk)
    return render (request,"home.html",{"book":book})
           
           
def show_book(request):
    books = Book.objects.all()
    return render(request,"show_book.html",{"all_books":books})

def delete_book(request,pk):
    book =Book.objects.get(id=pk)
    book.delete()
    return redirect("show-book")

def softdelete(request,pk):
    book = Book.objects.get(id=pk)
    book.is_available = 0
    book.save()
    return redirect("show-book")

def available_book(request):
    book = Book.objects.filter(is_available =True)
    return render(request,"show_book.html",{"all_books":book})

def unavailable_book(request):
    book = Book.objects.filter(is_available = False)
    return render(request,"show_book.html",{"all_books":book})


def login_page(request):
    if request.method=="POST":
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                messages.info(request,"you are logged in")
                return redirect("show-book")
            else:
                messages.error("invalid credinitals")
        else:
            messages.error(request,"check")
    form =AuthenticationForm()
    return render(request,"login.html",context={"login_form":form})
  
from .models import NewUserForm  
def register(request):
    if request.method =="POST":
        print(request.POST)
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            print(user)
            login(request,user)
            messages.success(request, "Registration successful." )
            return redirect("login")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render (request, "register.html", context={"register_form":form})
            
        
            

