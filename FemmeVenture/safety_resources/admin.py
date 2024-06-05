
# Register your models here.
from django.contrib import admin
from .models import SafetyResource

admin.site.register(SafetyResource)

#@admin.register(SafetyResource)
#class SafetyResourceAdmin(admin.ModelAdmin):
  #  list_display = ('title', 'category', 'created_at')
   # list_filter = ('category',)
