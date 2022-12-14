from django.contrib import admin
from .models import Venue
from .models import MyClubUser
from .models import Event
from .models import Room, Message

#admin.site.register(Venue)
admin.site.register(MyClubUser)
#admin.site.register(Event)

@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    list_display =  ('name', 'adress', 'phone')
    ordering = ('name',)
    search_fields = ('name', 'address')

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    fields = (('name', 'venue'), 'event_date', 'description', 'manager')
    list_display =  ('name', 'event_date', 'venue')
    list_filter = ('event_date', 'venue')
    ordering = ('-event_date',)

admin.site.register(Room)
admin.site.register(Message)
