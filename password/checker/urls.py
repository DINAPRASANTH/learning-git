from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('complete-profile/', views.complete_profile, name='complete_profile'),
    path('dashboard/', views.dashboard, name='dashboard'),  # <-- Add this if missing
    path('edit-profile/', views.edit_profile, name='edit_profile'),
    path('home/', views.dashboard, name='home')
]
