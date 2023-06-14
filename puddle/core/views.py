from django.shortcuts import render, redirect
from item.models import Category,Item

from django.contrib import auth
from .forms import SignupForm, User


# Create your views here.
def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()

    return render(request, 'core/index.html', {
        'categories': categories,
        'items': items,
    })
   

def contact(request):
    return render(request, 'core/contact.html')

def signup(request):
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = SignupForm()


    return render(request, 'core/signup.html', {
        'form' : form,
    })

def login(request):
    if request.method == 'POST':
        user_id = request.POST['username']
        pwd = request.POST['password']
        user = auth.authenticate(request, username=user_id, password=pwd)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            return render(request, "login.html", {
                'error': 'Username or Password is incorrect.',
            })
    else:
        return render(request, "login.html")

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        redirect('/')
    return render(request,'index.html')