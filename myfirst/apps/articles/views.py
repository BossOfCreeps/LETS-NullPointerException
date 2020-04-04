from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from .models import Event, Comment
from django.urls import reverse


def index(request):
    return render(request, 'index.html', {})


def events(request):
    all_events = Event.objects.order_by("id")
    return render(request, 'events.html', {"events": all_events})


def event(request, event_id):
    try:
        e = Event.objects.get(id=event_id)
    except:
        raise Http404()

    last_comments = e.comment_set.order_by("-id")

    return render(request, 'event.html', {"event": e, "comments": last_comments})


def add_comment(request, event_id):
    try:
        e = Event.objects.get(id=event_id)
    except:
        raise Http404()
    print(request.POST['name'])

    e.comment_set.create(author=request.POST['name'], text=request.POST['text'])
    return HttpResponseRedirect(reverse('event', args=(e.id,)))


def profile(request):
    pass


def reg(request):
    pass
