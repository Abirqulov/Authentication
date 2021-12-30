from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse

from django.contrib import messages

from .forms import OrderForm, CreateUserForm
from .models import *


def register_page(request):
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Accaunt was created for ' + user)

            return redirect('login')
    else:
            form = CreateUserForm()
    return render(request, 'register.html', {'form':form})


def login_page(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'username or password is incorrect')

    context = {}
    return render(request, 'login.html', context)


def home_page(request):
    if request.user.is_authenticated:
        restaurants = Restourant.objects.all()
        return render(request, 'home.html', {'restaurants': restaurants})
    else:
        return HttpResponseRedirect(reverse('login'))


def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))


def contact_page(request):
    return render(request, 'contact.html')


def about_page(request):
    return render(request, 'about.html')


def admin_page(request):
    return render(request, 'admin.html')


def restaran(request, pk_test):
    restaurant = Restourant.objects.filter(id=pk_test).first()
    food = FastFoodMenu.objects.filter(restaran=restaurant.id)
    categories = Category.objects.all()
    return render(request, 'restaran.html', {'food': food, 'rest': restaurant, 'categories': categories})


def category(request, cat_id):
    category = Category.objects.filter(id=cat_id).first()
    return render(request, 'restaran.html', {'category': category})


def see_more(request):
    menus = FastFoodMenu.objects.all()
    return render(request, 'see_more.html', {'menus': menus})


