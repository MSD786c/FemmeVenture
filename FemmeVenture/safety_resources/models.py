from django.db import models
from django.conf import settings

# Create your models here.

class SafetyResource(models.Model):
    CATEGORY_CHOICES = [
        ('SB', 'Safety Basics'),
        ('DS', 'Destination-Specific Safety Guides'),
        ('EC', 'Emergency Contacts and Resources'),
        ('SG', 'Safety Gear and Gadgets'),
        ('TS', 'Transportation Safety Tips'),
        ('CS', 'Community Safety Stories'),
    ]

    category = models.CharField(max_length=2, choices=CATEGORY_CHOICES)
    title = models.CharField(max_length=255)
    description = models.TextField()
    content = models.TextField(blank=True)  # For text-based content
    link = models.URLField(blank=True)  # For external resources or videos
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='liked_resources')
    card_img =  models.ImageField(null=True, blank=True,upload_to ='static/images/', default="static/images/SR3.png")
    main_img = models.ImageField(null=True, blank=True,upload_to ='static/images/', default="static/images/SR2.png")

    def __str__(self):
        return self.title

