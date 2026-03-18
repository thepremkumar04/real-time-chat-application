# chat/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    
    # FIX: Make sure there is NO "/history/" here
    path('api/messages/<str:room_name>/', views.room_history, name='room_history'),
]