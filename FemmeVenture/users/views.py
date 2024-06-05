from django.http import JsonResponse
from .models import Profile
from django.shortcuts import  render

def profiles(request):
    return render(request, 'profilecustom.html')


def profile(request):
    try:
        profiles = Profile.objects.all()
    except Exception as e:

        return render(request, 'error.html', {'error_message': str(e)})
    
    context = {'profiles': profiles}
    return render(request, 'buddyfinder.html', context)


def profile_view(request, username):
    return render(request, 'profilecustom.html', {'profile': profile})

from django.http import JsonResponse
from .models import Profile

def get_profiles(request):
    query = Profile.objects.all()

    # Applying filters
    activity = request.GET.get('activity')
    travel = request.GET.get('travel')
    goals = request.GET.get('goals')
    interests = request.GET.get('interests')

    if activity:
        query = query.filter(first_question_option=activity)
    if travel:
        query = query.filter(second_question_option=travel)
    if goals:
        query = query.filter(third_question_option=goals)
    if interests:
        query = query.filter(fourth_question_option=interests)

    # Log the query set count
    print("Filtered profiles count:", query.count())
    profiles = list(query.values('username', 'bio', 'profile_image', 'first_question_option', 'second_question_option', 'third_question_option', 'fourth_question_option'))

    # Check the actual data being returned
    print("Profiles data:", profiles)

    return JsonResponse(profiles, safe=False)
