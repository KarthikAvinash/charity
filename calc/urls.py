from audioop import add
from django.urls import path
from . import views
from django.contrib import admin
from .views import redirect_view 

urlpatterns = [
    path("register", views.register, name="register"),
    path("", views.login_user, name="login_user"),
    path("login_user", views.login_user, name="login_user"),

    path("logout", views.logout_user, name="logout_user"),
    path("home", views.ind, name="home"),

    path('',views.ind,name='Home_Page'),
    path('1',views.ind,name='Home_Page'),
    path('2',views.about,name='About'),
    path('3',views.add,name="adding"),
    path('4',views.student,name='Students time table'),
    path('5',views.faculty,name='facultys timetable'),
    path('6',views.contact,name='contact'),
    path('7',views.classroom,name='classroom'),
    path('8',views.lab,name="lab rooms"),
    path('endf',views.faculty,name='facultytime'),
    path('get',views.contact_upload,name='home'),
    path('end',views.student,name='ending'),
    path('100',views.refresh_page,name='refresh'),
    path('101',views.ref,name='refresh_only_added_details'),
    path('login',views.loginPage,name='login'),
    path('register',views.registerPage,name='register'),
    path('upload-csv/',views.contact_upload,name="upload csv"),
    path('upload-csv/dele',views.dele,name="redirect"),
    path('upload-csv/dele2',views.dele2,name="redirect"),
    path('dele2',views.dele2,name="lkjhgf"),
    path('dele',views.dele,name="lkjhgf"),
    path('/redirect/', redirect_view,name="redirecting"),
    path("",views.ind,name="returned"),
]
