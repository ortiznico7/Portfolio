from django.urls import path
from .views import MemberList, CreateMember
from django.urls import path
from .views import home

urlpatterns = [
    path('', MemberList.as_view(), name="member-list" ),
    path('create/', CreateMember.as_view(), name="member-create"),
    path('hello/',hello_myfinance,name="hello_myfin"),
    path('', home, name='home'),
] 

