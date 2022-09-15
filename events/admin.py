from django.contrib import admin
from .models import Venue
from .models import MyClubUser
from .models import Event
# El . quiere decir "en el mismo directorio", events/models.py

#admin.site.register(Venue)
admin.site.register(MyClubUser)
admin.site.register(Event)

@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    list_display =  ('name', 'adress', 'phone')
    ordering = ('name',) #ordena alfabéticamente lqs ve en admin
    search_fields = ('name', 'address')
