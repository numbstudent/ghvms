from django.urls import path
from hello_world import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register', views.register, name='register'),
    path('login', views.loginVendor, name='login'),
    path('logout', views.logoutVendor, name='logout'),
    # path('login',
        #  auth_views.LoginView.as_view(template_name='singlepage/login.html')),
    path('register-success', views.register_success),
    path('verification/<tokenurl>/<uuid>', views.register_verification),
    path('lupa', views.register_verification),
]
