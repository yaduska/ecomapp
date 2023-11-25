from django.urls import path
from django.contrib.auth import views as auth_views
from .views import contact,index,about,signup
from .forms import LoginForm

app_name='core'
urlpatterns=[
    path('',index,name='index'),
    path('contact/',contact,name='contact'),
    path('about/',about,name='about'),
    path('signup/',signup,name='signup'),
    path('login/',auth_views.LoginView.as_view(template_name='core/login.html',authentication_form=LoginForm),name='login')
]