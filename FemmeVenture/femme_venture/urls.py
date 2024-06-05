"""
URL configuration for femme_venture project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include  # new
from django.views.generic.base import TemplateView  # new
from ai import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("accounts.urls")),  # new
    path("accounts/", include("django.contrib.auth.urls")),  # new

    path("", include ("destinations.urls")), #layan
    path("", include ("users.urls")), #layan
    path("", include ("safety_resources.urls")), #Aaliyah
    path('', include('profCust.urls')), #krishna
    path('chat/', include('chat.urls')), #kenzy
    path('forum/', include('forum.urls')),
    path("", include("ai.urls")), # include this


    path("", TemplateView.as_view(template_name="index.html"), name="index"),  # new
    path("viewallcities", TemplateView.as_view(template_name="viewallcities.html"), name="viewallcities"),  # new
    path("forum", TemplateView.as_view(template_name="forum.html"), name="forum"),
    path("buddyfinder", TemplateView.as_view(template_name="buddyfinder.html"), name="buddyfinder"),
    path("hersafety", TemplateView.as_view(template_name="hersafety.html"), name="hersafety"),
    #path("chat", TemplateView.as_view(template_name="chat.html"), name="chat"),
    path("itineraryai", TemplateView.as_view(template_name="itineraryai.html"), name="itineraryai"),
    path("profile", TemplateView.as_view(template_name="profilecustom.html"), name="profilecustom"),
    path("destinations", TemplateView.as_view(template_name="destinations.html"), name="destinations"), #new
    path("ventures", TemplateView.as_view(template_name="ventures.html"), name="ventures"),
    path("favorites", TemplateView.as_view(template_name="favorites.html"), name="favorites"),


    path("gdpr", TemplateView.as_view(template_name="gdpr.html"), name="gdpr"),
    path("aboutus", TemplateView.as_view(template_name="aboutus.html"), name="aboutus"),

    
    path("hersafety", TemplateView.as_view(template_name="hersafety.html"), name="hersafety"),
    path("emergcontacts", TemplateView.as_view(template_name="emergcontacts.html"), name="emergcontacts"),
    path("safetygear", TemplateView.as_view(template_name="safetygear.html"), name="safetygear"),
    path("safetybasics", TemplateView.as_view(template_name="safetybasics.html"), name="safetybasics"),
    path("Transportation", TemplateView.as_view(template_name="Transportation.html"), name="Transportation"),
    path("CommunitySafety", TemplateView.as_view(template_name="CommunitySafety.html"), name="CommunitySafety"),
    path("destinationguides", TemplateView.as_view(template_name="destinationguides.html"), name="destinationguides"),
    path("post_create", TemplateView.as_view(template_name="post_create.html"), name="post_create"), #ashitha
    

    

    path('api-auth/', include('rest_framework.urls')),
    
    
    path("profilecustom", TemplateView.as_view(template_name="profilecustom.html"), name="profilecustom"),
#  path("profileEdit.html/",TemplateView.as_view(template_name="profEditing.html"),name="profileEdit"), #krishna new
   



]
