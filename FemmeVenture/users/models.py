from django.db import models
from django.contrib.auth.models import User
import uuid


# new

from django.db.models.signals import post_save, m2m_changed


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=500, blank=True, null=True)
    username = models.CharField(max_length=200, blank=True, null=True)
    bio = models.TextField(blank=True, null=False, default = '')
    profile_image = models.ImageField(null=False, blank=True,upload_to ='static/images/profiles/', default="static/images/profiles/user-default.png")
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)



    #krishna's changes to the model:
    first_name = models.CharField(max_length=200, blank=True, null=False , default='')
    last_name = models.CharField(max_length=200, blank=True, null=False , default='')
    occupation = models.CharField(max_length=100, blank=True, null=False , default='')
    location = models.CharField(max_length=100, blank=True, null= False , default='')
    # description = models.TextField(blank=True, null=True)

 

    first_question_option = models.CharField(max_length=100, choices=[ ("hiking", "Hiking"),
    ("water_sports", "Water sports"),
    ("camping", "Camping"),
    ("wildlife_safari", "Wildlife Safari"),
    ("skating", "Skating"),
    ("yoga_retreats", "Yoga retreats"),
    ("sunset_seeker", "Sunset seeker"),
    ("snow_boarding", "Snow Boarding")],null=True)
    
    
    second_question_option = models.CharField(max_length=100, choices=[  ("beach_destinations", "Beach destinations"),
    ("mountains_nature_retreats", "Mountains and Nature retreats"),
    ("urban_city_exploration", "Urban City exploration"),
    ("historical_cultural_sites", "Historical and cultural sites"),
    ("unique_cuisine", "Anywhere with unique cuisine"),
    ("tropical_island", "Tropical Island")],null=True)


    third_question_option = models.CharField(max_length=100, choices=[("self_discovery", "Self Discovery"),
        ("making_new_friends", "Making New Friends"),
        ("learning_about_cultures", "Learning About Different Cultures"),
        ("relaxation_reflection", "Relaxation and Reflection"),
        ("self_discipline", "Self Discipline"),
        ("practicing_meditation", "Practicing Meditation"),],null=True)



    fourth_question_option = models.CharField(max_length=100, choices=[    ("backpacking", "Backpacking"),
        ("surfing", "Surfing"),
        ("marathons", "Marathons"),
        ("food-cuisines", "Food cuisines"),
        ("journalling", "Journalling"),],null=True)
    
   
    # Followers and following relationships
    following = models.ManyToManyField('self', symmetrical=False, related_name='followers_reverse',blank=True)
    followers = models.ManyToManyField('self', symmetrical=False, related_name='following_reverse',blank=True)

    def get_following_profiles(self):
        return self.following.all()

    def get_followers_profiles(self):
        return self.followers.all()

    def __str__(self):
        return str(self.user.username)

    def __str__(self):
        return str(self.user.username)





#  Create a profile everytime a user signs up

def create_profile(sender,instance,created,**kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()
    
post_save.connect(create_profile,sender=User)


def update_followers(sender, instance, action, **kwargs):
    if action == 'post_remove':
        for followed_user in kwargs['pk_set']:
            followed_profile = Profile.objects.get(pk=followed_user)
            followed_profile.followers.remove(instance.pk)
    elif action == 'post_add':
        for followed_user in kwargs['pk_set']:
            followed_profile = Profile.objects.get(pk=followed_user)
            followed_profile.followers.add(instance.pk)