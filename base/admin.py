from django.contrib import admin
from .models import Profile, Group, Event, HousingListing, Message

admin.site.register(Profile)
admin.site.register(Group)
admin.site.register(Event)
admin.site.register(HousingListing)
admin.site.register(Message)
