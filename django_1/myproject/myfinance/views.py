from django.urls import reverse
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from .models import Member


class MemberList(ListView):
    template_name = "member_list.html"
    model = Member

class CreateMember(CreateView):
    template_name = "member_create.html"
    model = Member

def get_success_url(self) -> str:
    return reverse("member-list")