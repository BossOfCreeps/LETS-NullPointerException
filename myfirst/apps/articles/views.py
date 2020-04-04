from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from .models import Event, Comment, UserInfo
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
    user = " "
    try:
        user = request.GET['user']
    except:
        pass
    return render(request, 'profile.html', {"u": user})


def reg(request):
    pass


def test(request):

    extra_list = {1,3,4,6,8,10,12,14,19}
    result=0

    for i in range(1,21):
        if (i in extra_list) and (request.POST['id_'+str(i)]):
            result += 5
        if not (i in extra_list) and not (request.POST['id_'+str(i)]):
            result += 5

    result = result / 100
    u = UserInfo(name=request.GET['user'], test=result)
    u.save()
    return HttpResponseRedirect(reverse('profile'))

