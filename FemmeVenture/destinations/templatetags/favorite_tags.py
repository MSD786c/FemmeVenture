from django import template
from destinations.models import Favorite

register = template.Library()

@register.filter(name='is_favorite')
def is_favorite(city, user):
    if not user.is_authenticated:
        return False
    return Favorite.objects.filter(city=city, profile=user.profile).exists()
