#urls.py under profile customization application
from django.urls import path, include
from .views import profile_view , update_profile
from . import views

app_name = "profCust"

urlpatterns = [

    path('', profile_view, name='profile_customization'),  # Example URL for profile customization
    # path('profileEdit.html' , edit_profile , name = "edit_profile")
   
    path('profileEdit.html/', update_profile, name='update_profile',),
   
  
    path('profile/<int:pk>', views.profile, name='profile'),

    path('profile_list/',views.profile_list,name="profile_list"),
   

    path('profiles/<str:pk>', views.profile_view, name='profiles'),
 
    # path('profilecustom.html', update_profile, name='update_profile'),
    

]

    # Add more URLs as needed for profile customization

