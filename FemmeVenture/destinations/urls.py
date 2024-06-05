from django.urls import path
from . import views

name = 'destinations'


urlpatterns = [
    path('', views.cities, name="cities"), 
    path('index.html', views.cities, name="cities"),
   # path("search.html", views.search, name="search"), #aaliyah

    path('viewallcities', views.allcities, name="viewallcities"),

    path('city/<str:pk>/', views.city, name="city"), 
    
    path('city/venture/<str:pk>/', views.vent, name="vent"), 

    path('city/<str:pk>/delete_review/', views.delete_review, name="delete_review"),

    path('toggle-favorite/', views.toggle_favorite, name='toggle_favorite'),


    path('add_to_favorites/<str:pk>/', views.add_to_favorites, name='add_to_favorites'),
    path('remove_from_favorites/<str:pk>/', views.remove_from_favorites, name='remove_from_favorites'),
    path('favorites', views.view_favorites, name='view_favorites'),
    path('', views.cities, name="cities"), #a

]

