from django.urls import path
from .import views

urlpatterns = [
    path('signup/',views.signup,name='signup'),
    path('login/',views.login_view,name="login"),
    path('home/',views.home,name='home'),
    path('logout/',views.logout,name='lagout'),
    path('profile/',views.profile,name='profile')
]
