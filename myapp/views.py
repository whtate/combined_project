from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.conf import settings
import json
from django.core.serializers.json import DjangoJSONEncoder
from .models import Event
from .forms import EventForm
from datetime import datetime
from django.utils.timezone import make_aware

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after registration
            messages.success(request, 'Registration successful. You are now logged in.')
            return redirect('map')  # Redirect to group list or any desired page
    else:
        form = UserCreationForm()
    
    return render(request, 'registration/register.html', {'form': form})


@login_required
def map_view(request):
    events = Event.objects.all()
    events_data = json.dumps(list(events.values()), cls=DjangoJSONEncoder)

    context = {
        'events': events,
        'mapbox_access_token': settings.MAPBOX_ACCESS_TOKEN,
    }
    return render(request, 'myapp/map.html', context)

@login_required
def add_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.created_by = request.user  # Set the user creating the event
            event.save()
            messages.success(request, 'Event added successfully!')
            return redirect('map')
    else:
        form = EventForm()
    return render(request, 'myapp/add_event.html', {'form': form})





