from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import login as django_login, authenticate
from django.contrib.auth import logout
from .models import Blog


# Create your views here.


def index(request):
    blog = Blog.objects.all()
    return render(request, 'index.html', {'blogs':blog})


def register(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        username = request.POST.get('username')
        if User.objects.filter(email=email).exists():
            messages.warning(request, 'email is already exists')
            return redirect('register')
        else:
            user = User(email=email, password=password,
                        first_name=firstname, last_name=lastname, username=username)
            user.set_password(password)
            user.save()
            messages.success(request, 'User Has Been Registered Successfully.')
            return redirect('login')
    return render(request, 'register.html')


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            django_login(request, user)
            return redirect("/")
        else:
            messages.warning(request, 'Invalid Credentials')
            return redirect('login')
    return render(request, 'login.html')


def logout_user(request):
    logout(request)
    return redirect('login')

def blogpost(request):
    if request.method == "POST":
        title =request.POST.get("title") 
        content =request.POST.get("content")
        blog = Blog(title=title, content=content,user_id=request.user)
        blog.save()
        messages.success(request,"Post has been submitted successfully")
        return redirect("/") 
    return render(request,'blogpost.html')

def blog_detail(request, id):
    blog = Blog.objects.get(id=id)
    return render(request,'blog_detail.html',{'blog':blog})

def delete_post(request, id):
    blog = Blog.objects.get(id=id)
    print(blog)
    blog.delete()
    messages.success(request,'Post has been deleted successfully')
    return redirect("/")


