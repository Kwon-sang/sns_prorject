from django.urls import path

from . import views

urlpatterns = [
    path('signup/', views.signup, name='sign_up'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('edit/', views.profile_edit, name='profile_edit'),
]