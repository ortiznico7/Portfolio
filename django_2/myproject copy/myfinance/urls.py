from django.urls import path, include
from .views import MemberList, CreateMember
from .views import home
from django.contrib.auth import views as auth_views
from . import views
from django.contrib import admin

urlpatterns = [
    path('', MemberList.as_view(), name="member-list" ),
    path('create/', CreateMember.as_view(), name="member-create"),
    path('hello/', views.hello_myfin, name="hello_myfin"),
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
] 
