from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from .models import Event


def index(request):
    return render(request, 'index.html', {})


def events(request):
    all_events = Event.objects.order_by("id")
    return render(request, 'events.html', {"events": all_events})


def event(request, event_id):
    try:
        e = Event.objects.get(id=event_id)
    except:
        raise Http404("error")

    return render(request, 'event.html', {"event": e})
