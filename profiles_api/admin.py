from django.contrib import admin
from .models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    # Define any customizations for the admin interface
    search_fields = ['name']
    pass

admin.site.register(UserProfile, UserProfileAdmin)
