from django.db import models
import uuid
from users.models import Profile

#from user.models import Profile

# Create your models here.

class City(models.Model):
    title = models.CharField(max_length=200)
    countryname = models.CharField(max_length=200)
    demo_link = models.CharField(max_length=2000, null=True, blank=True)
    rate_total = models.IntegerField(default=0,  null=True, blank=True)
    rate_average = models.FloatField(default=0, null=True, blank=True)
    card_img =  models.ImageField(null=True, blank=True,upload_to ='static/images/destinations/', default="static/images/destinations/luc2.png")
    main_img = models.ImageField(null=True, blank=True,upload_to ='static/images/destinations/', default="static/images/destinations/alps.png")
    

    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.title
    
    def reviewers(self):
        queryset = self.review_set.all().values_list('owner__id', flat=True)
        return queryset
    
    
    @property
    def getVotes(self):
        reviews = self.review_set.all()
        total_rates = reviews.count()
        if total_rates > 0:
            rate_sum = sum(review.value for review in reviews)
            self.rate_average = rate_sum / total_rates
        else:
            self.rate_average = 0  # No reviews left, set average to zero

        self.rate_total = total_rates
        self.save()




class Review(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    body = models.TextField(null=True, blank=True)
    value = models.FloatField(default=1, choices=((1, '1 Star'),
                                                                (2, '2 Stars'),
                                                                (3, '3 Stars'),
                                                                (4, '4 Stars'),
                                                                (5, '5 Stars'),))
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    class Meta:
        unique_together = [['owner', 'city']]

    def __str__(self):
        return f"{self.owner} - {self.city} - {self.value} Star" + ("s" if self.value > 1 else "")
    


class Ventures(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=True, default="Coming Soon")
    body = models.TextField(null=True, blank=True)
    venture_img = models.ImageField(null=True, blank=True,upload_to ='static/images/destinations/', default="static/images/destinations/defaultvent.png")
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    
    def __str__(self):
        return f"{self.title} - {self.city}"


class Feedback(models.Model):
    owner = models.OneToOneField(Profile, on_delete=models.CASCADE, null=True)  # Changed to OneToOneField
    body = models.TextField(null=True, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return f"{self.owner} - {self.body}"



class Favorite(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('profile', 'city')  # Ensure a user can only favorite a city once

    def __str__(self):
        return f"{self.profile.user.username} likes {self.city.title}"