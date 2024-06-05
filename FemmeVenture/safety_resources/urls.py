from django.urls import path
from . import views
from .views import resources


urlpatterns = [
    path('', views.resources, name="resources"),
    path('safetybasics', views.resources, name="resources"),
    path('destinationguides', views.destination_guides, name="destination_guides"),
    path('emergcontacts', views.emergcontacts, name="emergcontacts"),
    path('safetygear', views.safetygear, name="safetygear"),
    path('CommunitySafety', views.CommunitySafety, name="CommunitySafety"),
    path('Transportation', views.Transportation, name="Transportation"),
    path('like_resource/<title>/<category>/', views.like_resource, name='like_resource'),
    
    
    
]
