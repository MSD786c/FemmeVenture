#models.py under profile customization application
from django.db import models

# Create your models here.

# In models.py of the profile_customization app

from django.contrib.auth import get_user_model

from users.models import Profile

User = get_user_model()

class UserProfile(models.Model):
    # user_instance = models.ForeignKey(Profile, on_delete=models.CASCADE, default = None)
  
   # user_profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    user_profile = models.OneToOneField(Profile, on_delete=models.CASCADE, )

    # Additional fields for profile customization
    first_name = models.CharField(max_length=200, blank=True, null=True)
    last_name = models.CharField(max_length=200, blank=True, null=True)
    occupation = models.CharField(max_length=100, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    id = models.IntegerField(primary_key=True)

   
    # Add more fields as needed for customization options
    # Radio button options for the first question
    first_question_option = models.CharField(max_length=100, choices=[ ("hiking", "Hiking"),
    ("water_sports", "Water sports"),
    ("camping", "Camping"),
    ("wildlife_s.exitafari", "Wildlife Safari"),
    ("skating", "Skating"),
    ("yoga_retreats", "Yoga retreats"),
    ("sunset_seeker", "Sunset seeker"),
    ("snow_boarding", "Snow Boarding")])
    
    # Radio button options for the second question
    second_question_option = models.CharField(max_length=100, choices=[  ("beach_destinations", "Beach destinations"),
    ("mountains_nature_retreats", "Mountains and Nature retreats"),
    ("urban_city_exploration", "Urban City exploration"),
    ("historical_cultural_sites", "Historical and cultural sites"),
    ("unique_cuisine", "Anywhere with unique cuisine"),
    ("tropical_island", "Tropical Island")])

    # Radio button options for the third question
    third_question_option = models.CharField(max_length=100, choices=[("self_discovery", "Self Discovery"),
        ("making_new_friends", "Making New Friends"),
        ("learning_about_cultures", "Learning About Different Cultures"),
        ("relaxation_reflection", "Relaxation and Reflection"),
        ("self_discipline", "Self Discipline"),
        ("practicing_meditation", "Practicing Meditation"),])


    # Radio button options for the third question
    fourth_question_option = models.CharField(max_length=100, choices=[    ("backpacking", "Backpacking"),
        ("surfing", "Surfing"),
        ("marathons", "Marathons"),
        ("food-cuisines", "Food cuisines"),
        ("journalling", "Journalling"),])
    

    # Add more fields for additional questions as needed

    def __str__(self):
        return self.user_profile.user.username

