from django.urls import path
from .views import forum, post_create, like_post, submit_reply

urlpatterns = [
    path('', forum, name='forum'),
    path('post_create/', post_create, name='post_create'),
    path('like-post/', like_post, name='like_post'),
    path('submit-reply/', submit_reply, name='submit_reply')

]                                                                                                      
