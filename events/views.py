from django.shortcuts import render, redirect
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from django.http import HttpResponseRedirect
from .models import Event, Venue
from .forms import VenueForm, EventForm
<<<<<<< HEAD
from django.views.generic import TemplateView
=======
from .models import Room, Message
from django.http import HttpResponse, JsonResponse
>>>>>>> 2bea1d1bb4b771d984eac83ae3eaf2d78937143f

def about_us(request):
    return render(request, 'events/about_us.html')

def delete_venue(request, venue_id):
    venue = Venue.objects.get(pk=venue_id)
    venue.delete()
    return redirect('list-venues')

def delete_event(request, event_id):
    event = Event.objects.get(pk=event_id)
    event.delete()
    return redirect('event-list')


def add_event(request):
    submitted = False
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/add_event?submitted=True')
    else:
        form = EventForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'events/add_event.html', {'form': form, 'submitted': submitted})


def update_event(request, event_id):
	event = Event.objects.get(pk=event_id)
	form = EventForm(request.POST or None, instance=event)
	if form.is_valid():
		form.save()
		return redirect('event-list')

	return render(request, 'events/update_event.html',
               {'event': event,
                'form': form})


def update_venue(request, venue_id):
	venue = Venue.objects.get(pk=venue_id)
	form = VenueForm(request.POST or None, request.FILES or None, instance=venue)
	if form.is_valid():
		form.save()
		return redirect('list-venues')

	return render(request, 'events/update_venue.html',
               {'venue': venue,
                'form': form})

def search_venues(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        venues = Venue.objects.filter(name__contains=searched)
        return render(request, 'events/search_venues.html',
{'searched': searched, 'venues':venues})
    else:
        return render(request, 'events/search_venues.html',
{})


def show_venue(request, venue_id):
    venue = Venue.objects.get(pk=venue_id)
    return render(request, 'events/show_venue.html',
        {'venue': venue})


def list_venues(request):
    venue_list = Venue.objects.all()
    return render(request, 'events/venue.html',
        {'venue_list': venue_list})

def add_venue(request):
    submitted = False
    if request.method == "POST":
        form = VenueForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_venue?submitted=True') 
    else:
        form = VenueForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'events/add_venue.html', {'form':form, 'submitted':submitted})

def all_events(request):
    event_list = Event.objects.all()
    return render(request, 'events/event_list.html',
                  {'event_list': event_list})


def home(request, year=datetime.now().year, month=datetime.now().strftime('%B')):
    month = month.capitalize()
    month_number = list(calendar.month_name).index(month)
    month_number = int(month_number) 

    cal = HTMLCalendar().formatmonth(year, month_number)
    name = 'User'
    now = datetime.now()
    current_year = now.year
    time = now.strftime('%I:%M:%S %p')

    return render(request, 'events/home.html', {
        'first_name': name,
        'year': year,
        'month': month,
        'month_number': month_number,
        'cal': cal, 
        'current_year': current_year,
        'time': time,
    })

<<<<<<< HEAD
class Error404View (TemplateView):
    template_name = "events/error404.html"
=======
def messages(request):
    return render(request,'events/messages.html')

def room(request, room):
    username = request.GET.get('username')
    room_details = Room.objects.get(name=room)
    return render(request, 'events/room.html', {
        'username': username,
        'room': room,
        'room_details': room_details
    })

def checkview(request):
    room = request.POST['room_name']
    username = request.POST['username']

    if Room.objects.filter(name=room).exists():
        return redirect('/'+room+'/?username='+username)
    else:
        new_room = Room.objects.create(name=room)
        new_room.save()
        return redirect('/'+room+'/?username='+username)

def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']

    new_message = Message.objects.create(value=message, user=username, room=room_id)
    new_message.save()
    return HttpResponse('Message sent successfully')

def getMessages(request, room):
    room_details = Room.objects.get(name=room)

    messages = Message.objects.filter(room=room_details.id)
    return JsonResponse({"messages":list(messages.values())})
>>>>>>> 2bea1d1bb4b771d984eac83ae3eaf2d78937143f
