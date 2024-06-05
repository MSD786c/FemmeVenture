from django.db.models import Exists, OuterRef
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# Create your views here.

from .models import City
from .forms import ReviewForm, FeedbackForm
from django.contrib import messages
from .models import Ventures
from .models import Feedback, Review, Favorite
from django import forms

from users.models import Profile 


def cities(request):
    
    user = request.user
    if user.is_authenticated:
        profile = user.profile
        didfeedback = Feedback.objects.filter(owner=profile).exists()
        
        cities = City.objects.all().order_by('-rate_average')[:8] #a
       

        # Prepare a subquery to check if each city is favorited by this user
        favorites_subquery = Favorite.objects.filter(
            profile=profile,
            city=OuterRef('pk')
        )
        cities = City.objects.annotate(
            is_favorited=Exists(favorites_subquery)
        ).order_by('-rate_average')[:8]

        if not didfeedback:
            if request.method == 'POST':
                form = FeedbackForm(request.POST)
                if form.is_valid():
                    feedback = form.save(commit=False)
                    feedback.owner = profile
                    feedback.save()
                    messages.success(request, 'Feedback submitted successfully!')
                    return redirect('index')  # Redirect using the name of your URL pattern
            else:
                form = FeedbackForm()
        else:
            form = FeedbackForm()
    else:
        cities = City.objects.all().order_by('-rate_average')[:8]
        form = FeedbackForm()
        didfeedback = False  # Ensure this is false if user is not authenticated

    feedbacks = Feedback.objects.all()

    context = {
        'cities': cities,
        'feedbacks': feedbacks,
        'form': form,
        'didfeedback': didfeedback
    }
    return render(request, 'index.html', context)

def city(request, pk):
    cityObj = City.objects.get(id=pk)
    form = ReviewForm(request.POST or None)
    ventures = Ventures.objects.filter(city=cityObj)  

    
    if request.method == 'POST':
        if form.is_valid():
            review = form.save(commit=False)
            review.city = cityObj
            review.owner = request.user.profile  # Adjust according to your user profile setup
            review.save()

            cityObj.getVotes



            messages.success(request, 'Your review was successfully submitted!')
            return redirect('city' , pk=cityObj.id)
        else:
            # The form is not valid, render the page with the form to show validation errors
            return render(request, 'destinations.html', {'cityObj' : cityObj, 'form' : form })

    else:
        # GET request, render the page with an empty form
        form = ReviewForm()

    return render(request, 'destinations.html', {'cityObj' : cityObj, 'form' : form, 'ventures': ventures })



        #update city count 


def vent(request, pk):
    ventObj = Ventures.objects.get(id=pk)
    

    context = {
        'ventObj': ventObj,
    }
    
    return render(request, 'ventures.html', context)



def allcities(request):

    user = request.user
    if user.is_authenticated:
        profile = user.profile

        # Prepare a subquery to check if each city is favorited by this user
        favorites_subquery = Favorite.objects.filter(
            profile=profile,
            city=OuterRef('pk')
        )
        allcities = City.objects.annotate(
            is_favorited=Exists(favorites_subquery)
        ).order_by('-rate_average')

    context = {
        'allcities': allcities
    }
    return render(request, 'viewallcities.html', context)


def delete_review(request, pk):
    
    review = Review.objects.filter(owner=request.user.profile, city_id=pk).first()
    if review:
        city = review.city
        review.delete()
        city.getVotes  # Recalculate the votes for the city
        messages.success(request, "Your review has been deleted.")
    else:
        messages.error(request, "Review not found.")

    return HttpResponseRedirect(reverse('city', args=[pk]))




@login_required
def add_to_favorites(request, pk):
    city = get_object_or_404(City, pk=pk)
    Favorite.objects.get_or_create(profile=request.user.profile, city=city)
    messages.success(request, f'{city.title} has been added to your favorites!')
    return redirect('index')  # Redirect to the list of cities

@login_required
def remove_from_favorites(request, pk):
    city = get_object_or_404(City, pk=pk)
    Favorite.objects.filter(profile=request.user.profile, city=city).delete()
    messages.success(request, f'{city.title} has been removed from your favorites!')
    return redirect('index')

@login_required
def view_favorites(request):
    user_profile = request.user.profile
    favorites = Favorite.objects.filter(profile=user_profile).select_related('city')
    
    # Always pass favorites, even if it's an empty queryset
    context = {'favorites': favorites}
    return render(request, 'favorites.html', context)

from django.http import JsonResponse
from django.views.decorators.http import require_POST



@login_required
@require_POST
def toggle_favorite(request):
    city_id = request.POST.get('city_id')
    city = get_object_or_404(City, id=city_id)
    favorite, created = Favorite.objects.get_or_create(profile=request.user.profile, city=city)

    if not created:
        favorite.delete()
        favorited = False
    else:
        favorited = True

    return JsonResponse({'favorited': favorited, 'city_id': city_id})
