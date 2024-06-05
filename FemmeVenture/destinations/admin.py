from django.contrib import admin

# Register your models here.
from .models import City
from .models import Review
from .models import Ventures
from .models import Feedback
from .models import Favorite

admin.site.register(City)
admin.site.register(Review)
admin.site.register(Ventures)
admin.site.register(Feedback)
admin.site.register(Favorite)

