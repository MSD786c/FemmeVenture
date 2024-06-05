from django.db import models

# Create your models here.

from django.contrib.auth.models import User
import uuid


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    city_country = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    content = models.TextField()
    comments_count = models.PositiveIntegerField(default=0)
    date = models.IntegerField()
    month = models.IntegerField()
    year = models.IntegerField()

    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.title                   

class Reply(models.Model):
    post = models.ForeignKey(Post, related_name='replies', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)