from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponse
from .models import SafetyResource
from django.http import JsonResponse

@login_required
def like_resource(request, title, category):
    if request.method == 'POST':
        resource = get_object_or_404(SafetyResource, title=title, category=category)
        # Assuming you have a ManyToMany field 'likes' in SafetyResource model relating to the User model
        if request.user in resource.likes.all():
            resource.likes.remove(request.user)  # Toggle like
        else:
            resource.likes.add(request.user)  # Toggle like
        resource.save()  # Save the changes
        return JsonResponse({'likes': resource.likes.count()})
    else:
        return JsonResponse({'error': 'This is not a POST request'}, status=400)


def resources(request, category ='SB'):
    resources = SafetyResource.objects.filter(category=category)
    context = {'resources': resources}
    return render(request, 'safetybasics.html', context)

def destination_guides(request, category ='DS'):
    resources = SafetyResource.objects.filter(category=category)
    context = {'resources': resources}
    return render(request, 'destinationguides.html', context)

def emergcontacts(request, category ='EC'):
    resources = SafetyResource.objects.filter(category=category)
    context = {'resources': resources}
    return render(request, 'emergcontacts.html', context)

def safetygear(request, category ='SG'):
    resources = SafetyResource.objects.filter(category=category)
    context = {'resources': resources}
    return render(request, 'safetygear.html', context)

def CommunitySafety(request, category ='CS'):
    resources = SafetyResource.objects.filter(category=category)
    context = {'resources': resources}
    return render(request, 'CommunitySafety.html', context)

def Transportation(request, category ='TS'):
    resources = SafetyResource.objects.filter(category=category)
    context = {'resources': resources}
    return render(request, 'Transportation.html', context)


