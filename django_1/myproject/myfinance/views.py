from django.urls import reverse
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from .models import Member
from django.http import HttpResponse
from django.contrib import admin
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

class MemberList(ListView):
    template_name = "member_list.html"
    model = Member

class CreateMember(CreateView):
    template_name = "member_create.html"
    model = Member

def get_success_url(self) -> str:
    return reverse("member-list")

def hello_myfin(request):
    return render(request, 'hellomyfinance/hello_myfinance.html')

def home(request):
    context = {'message': 'Welcome to MyFINANCE App!'}
    return render(request, 'home.html', context)

def hello_myfin(request):
    return HttpResponse("Hello from MyFinance app!")

def hello_myfinance(request):
    return HttpResponse("Hello from MyFinance!")

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            form = UserCreationForm()
        return render(request, 'register.html', {'form': form})