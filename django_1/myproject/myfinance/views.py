from django.urls import reverse
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from .models import Member
from django.http import HttpResponse


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

def hello_myfinance(request):
    return HttpResponse("Hello from MyFinance!")