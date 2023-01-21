from django.urls import path

from . import views

urlpatterns = [
        path('accounts/signup/', views.signup, name='signup'),
        path('accounts/login/', views.signin, name='login'),
        path('accounts/logout/', views.signout, name='logout')
]