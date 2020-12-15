from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.urls import path
from django.views.generic import TemplateView

import users.views as user_views

admin.autodiscover()
admin.site.login = login_required(admin.site.login)


urlpatterns = [
    path('test/',TemplateView.as_view(template_name='users/main.html')),
    path('admin/', admin.site.urls, name='#'),
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
]
