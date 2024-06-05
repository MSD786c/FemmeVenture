#views.py under profile customization application

from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from users.models import Profile
from itertools import chain
from django.shortcuts import get_object_or_404
import random
# Create your views here.

from users.models import Profile
from .forms import UserProfileUpdateForm
from django.urls import reverse

# Create your views here.

#from users.models import Profile
from .forms import UserProfileUpdateForm
from django.contrib import messages
import uuid


# def profile_view(request, pk):
#      follower = request.user.username
#      user = pk

#      if FollowersCount.objects.filter(follower=follower, user=user).first():
#         button_text = 'Unfollow'
#      else:
#         button_text = 'Follow'

#      user_followers = len(FollowersCount.objects.filter(user=pk))
#      user_following = len(FollowersCount.objects.filter(follower=pk))

#      profile_instance = Profile.objects.get(user= request.user)
#      context = {
#         'button_text': button_text,
#         'user_followers': user_followers,
#         'user_following': user_following,
#     }
#      return render(request, 'profilecustom.html', {' profile_instance':  profile_instance})


@login_required
def profile_view(request,username):
  user = get_object_or_404(User, username=username)
  profile_instance = user.profile
  return render(request, 'profileViews.html', {'profile_instance': profile_instance})




def update_profile(request):
    if request.method == 'POST':
        form = UserProfileUpdateForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            profile = request.user.profile
            cleaned_data = form.cleaned_data


             
            if not all(cleaned_data.values()):
                 # If any cleaned data is empty, reload the form without saving
                messages.error(request, "Please fill in all the fields!")
                return render(request, 'profEditing.html', {'form': form})
            
            for field_name in ['first_question_option', 'second_question_option', 'third_question_option', 'fourth_question_option']:
                if not cleaned_data.get(field_name):
                   messages.error(request, "Please fill all the option questions!")
                   return render(request, 'profEditing.html', {'form': form})
                
            
            
            if (cleaned_data['first_name']) :
                profile.first_name = cleaned_data['first_name']
            else:
                cleaned_data['first_name'] = profile.first_name

            if cleaned_data['last_name'] :
                profile.last_name = cleaned_data['last_name']
            else:
                cleaned_data['last_name'] = profile.last_name

            if cleaned_data['occupation'] :
                profile.occupation = cleaned_data['occupation']
            else:
                cleaned_data['occupation'] = profile.occupation

            if cleaned_data['location'] :
                profile.location = cleaned_data['location']
            else:
                cleaned_data['location'] = profile.location

            if cleaned_data['bio'] :
                profile.bio = cleaned_data['bio']
            else:
                cleaned_data['bio'] = profile.bio

            if cleaned_data['first_question_option'] :
                profile.first_question_option = cleaned_data['first_question_option']
            else:
                cleaned_data['first_question_option'] = profile.first_question_option

            if cleaned_data['second_question_option'] :
                profile.second_question_option = cleaned_data['second_question_option']
            else:
                cleaned_data['second_question_option'] = profile.second_question_option

            if cleaned_data['third_question_option'] :
                profile.third_question_option = cleaned_data['third_question_option']
            else:
                cleaned_data['third_question_option'] = profile.third_question_option

            if cleaned_data['fourth_question_option'] :
                profile.fourth_question_option = cleaned_data['fourth_question_option']
            else:
                cleaned_data['fourth_question_option'] = profile.fourth_question_option

            if 'profile_image' in request.FILES:
                profile.profile_image = request.FILES['profile_image']

            
            profile.save()

            messages.success(request, "Changes saved successfully. Click on Finish changes to go back to Profile View!")
            return render(request, 'profEditing.html', {'form': form})
        
        else:
        # Render form again for invalid data
          messages.error(request, "Please fill in all fields and select options for all questions!")
          return render(request, 'profEditing.html', {'form': form})
    else:
        form = UserProfileUpdateForm(instance=request.user.profile)
        return render(request, 'profEditing.html', {'form': form})


def profile_list(request):
    profiles= Profile.objects.exclude(user = request.user)

    return render(request,'profile_list.html',{profiles:profiles})



def profile(request,pk):
      acc = User.objects.get(id=pk) 



# hk
      if request.user == acc:
        # If the requested user is the current user, render profile_custom.html
        return render(request, "profilecustom.html")



      if request.method == "POST":
          #get current user id
          current_user_profile = request.user.profile
          #get form data
          action = request.POST['follow']

          if action == "unfollow":
              current_user_profile.following.remove(acc.profile)
              acc.profile.followers.remove(current_user_profile)
          elif action == "follow":
              current_user_profile.following.add(acc.profile)
              acc.profile.followers.add(current_user_profile)
          current_user_profile.save()
          acc.save()

      return render (request,"profile.html", {"acc" : acc})


