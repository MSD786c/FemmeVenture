from django.urls import path 
from . import views 

urlpatterns = [

    path('', views.profiles, name="profiles"),
    path('buddyfinder', views.profile, name="profiles"),
    path('profile/<str:username>/', views.profile_view, name='profile'),
    path('api/profiles/', views.get_profiles, name='get_profiles'),  # New API endpoint for AJAX


]