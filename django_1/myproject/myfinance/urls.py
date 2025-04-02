from django.urls import path, include
from .views import MemberList, CreateMember
from .views import home
from . import views
from django.contrib import admin

urlpatterns = [
    path('', MemberList.as_view(), name="member-list" ),
    path('create/', CreateMember.as_view(), name="member-create"),
    path('hello/', views.hello_myfin, name="hello_myfin"),
    path('', home, name='home'),
    path('admin/', admin.site.urls)
] 

