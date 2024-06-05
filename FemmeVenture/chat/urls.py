from django.urls import path
from . import views


urlpatterns = [
    path('', views.messages_page, name="messages_page"),
    path('thread_allocate', views.thread_allocate, name="thread_allocate"),
    path('ChatSearchBar', views.ChatSearchBar, name="ChatSearchBar"),
]