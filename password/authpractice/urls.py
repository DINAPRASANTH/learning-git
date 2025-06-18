from django.urls import path
from . import views

urlpatterns = [
    
    path('login/',views.my_login_view,name='my_login'),
    
]
