from django.urls import path, include
from django.contrib.auth import views as auth_views
from user import views as user_views


urlpatterns = [
    path('login/' , user_views.Login , name = 'Login'),
    path('register/' , user_views.register , name = 'register'),
    path('register-success/' , user_views.register_success, name = 'register-success'),
    path('logout/' , auth_views.LogoutView.as_view(template_name = 'home/homepage.html'))
]


