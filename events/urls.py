from django.urls import path
from . import views


urlpatterns = [
path('', views.home, name='home'),
    path('<int:year>/<str:month>/', views.home, name='home'),
    path('events', views.all_events, name='event-list'), 
    path('add_venue', views.add_venue, name='add-venue'),
    path('list_venues', views.list_venues, name='list-venues'),
    path('show_venue/<venue_id>', views.show_venue, name='show-venue'),
    path('search_venues', views.search_venues, name='search-venues'),
    path('update_venue/<venue_id>', views.update_venue, name='update-venue'),
    path('update_event/<event_id>', views.update_event, name='update-event'),
    path('add_event', views.add_event, name='add-event'),
    path('delete_event/<event_id>', views.delete_event, name='delete-event'),
    path('delete_venue/<venue_id>', views.delete_venue, name='delete-venue'),
    path('about_us', views.about_us, name='about-us'),
    path('messages/', views.messages, name='messages'),
    path('<str:room>/', views.room, name='room'),
    path('messages/checkview', views.checkview, name='checkview'),
    path('send', views.send, name='send'),
    path('getMessages/<str:room>/', views.getMessages, name='getMessages'),
]
