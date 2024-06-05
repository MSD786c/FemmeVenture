from django.db import models
from django.contrib.auth import get_user_model
from django.db.models import Q
from users.models import Profile

User = get_user_model()

# Create your models here.

class ThreadManager(models.Manager):
    def by_user(self, **kwargs):
        user = kwargs.get('user')
        lookup = Q(first_person=user) | Q(second_person=user)
        qs = self.get_queryset().filter(lookup).distinct()
        return qs


class Thread(models.Model):
    first_person = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='thread_first_person')
    second_person = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True,
                                     related_name='thread_second_person')
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    Additional_Note = models.CharField(max_length=255, blank=True, null=True)

    objects = ThreadManager()
    class Meta:
        unique_together = ['first_person', 'second_person']

    def first_person_profile(self):
        try:
            return Profile.objects.get(user = self.first_person)
        except:
            return None

    def second_person_profile(self):
        try:
            return Profile.objects.get(user = self.second_person)
        except:
            return None


class ChatMessage(models.Model):
    thread = models.ForeignKey(Thread, null=True, blank=True, on_delete=models.CASCADE, related_name='chatmessage_thread')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)