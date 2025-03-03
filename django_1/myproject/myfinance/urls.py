from django.urls import path
from .views import MemberList, CreateMember

urlpatterns = [
    path('', MemberList.as_view(), name="member-list" ),
    path('create/', CreateMember.as_view(), name="member-create")
] 
