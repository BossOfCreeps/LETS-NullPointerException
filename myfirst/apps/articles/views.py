# request.user.username
from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from .models import Event, Comment, UserInfo, Invite, ChatID, Chat
from django.urls import reverse
from django.contrib.auth.models import User
import os
from django.conf import settings
from django.core.files.storage import default_storage

delta_ungi = 0.2
UPLOAD_FOLDER = "/home/ubuntu/LETS-NullPointerException/static/img/events/"
ip = "89.208.220.42"

def index(request):
    return render(request, 'index.html', {})


def events(request):
    all_events = Event.objects.order_by("time")
    return render(request, 'events.html', {"events": all_events})


def event(request, event_id):
    try:
        e = Event.objects.get(id=event_id)
    except:
        raise Http404()

    try:
        comment_id = request.GET['id']
        Comment.objects.get(id=comment_id).delete()
    except:
        pass

    user_invites = list()
    for u in Invite.objects.filter(name1=request.user.username, event=event_id):
        print(u.name2)
        user_invites.append(u.name2)

    last_comments = e.comment_set.order_by("-id")

    return render(request, 'event.html', {"event": e, "comments": last_comments, 'invites': user_invites})


def add_comment(request, event_id):
    try:
        e = Event.objects.get(id=event_id)
    except:
        raise Http404()

    e.comment_set.create(author=request.user.username, text=request.POST['text'])
    return HttpResponseRedirect(reverse('event', args=(e.id,)))


def invite(request, event_id):
    name1 = request.user.username
    name2 = request.GET['user']
    Invite(name1=name1, name2=name2, event=event_id, e_name=Event.objects.get(id=event_id).name, submit=False).save()
    return HttpResponseRedirect(reverse('event', args=(event_id,)))


def profile(request):
    global delta_ungi
    user = request.user.username
    test = -1
    try:
        user = request.GET['user']
    except:
        pass
    try:
        test = UserInfo.objects.get(name=user).test
    except:
        pass
    invites = Invite.objects.filter(name2=user)
    my_invites = Invite.objects.filter(name1=user, submit=2)
    test_users = UserInfo.objects.filter()
    all_events = Event.objects.filter()
    users_list = list()
    for tu in test_users:
        if test + delta_ungi > tu.test > test - delta_ungi and tu.name != user:
            users_list.append(tu.name)

    chat = list()
    chat_id = -1


    if user != request.user.username:

        try:
            chat_id = ChatID.objects.get(name1=request.user.username, name2=request.GET['user']).chat_id
        except:
            chat_id = ChatID.objects.order_by('-id')[0].chat_id+1
            ChatID(name1=request.user.username, name2=request.GET['user'], chat_id=chat_id).save()
            ChatID(name2=request.user.username, name1=request.GET['user'], chat_id=chat_id).save()

        try:
            text = request.POST["message"]
            Chat(chat_id=chat_id, name=request.user.username, text=text).save()
        except:
            pass

        try:
            chat = Chat.objects.filter(chat_id=chat_id)
        except:
            pass


    return render(request, 'profile.html', {"u": user, "test": test, "invites": invites, "my_invites": my_invites,
                                            "test_users": users_list, "events": all_events, "chat": chat})


def reg(request):
    print(1)

    try:
        login = request.POST["login"]
        print(2)
        password = request.POST["pass"]
        print(3)
        try:
            User.objects.get(username=login)
            return render(request, 'reg.html', {"ok": False})
        except:
            User.objects.create_user(login, " ", password).save()
            return HttpResponseRedirect(reverse('index'))
    except:
        return render(request, 'reg.html', {"ok": True})


def test(request):
    extra_list = {1, 3, 4, 6, 8, 10, 12, 14, 19}
    result = 0

    for i in range(1, 21):
        if (i in extra_list) and int(request.POST['id_' + str(i)]):
            result += 5
            print(i, int(request.POST['id_' + str(i)]), 1)
        if not (i in extra_list) and not int(request.POST['id_' + str(i)]):
            result += 5
            print(i, int(request.POST['id_' + str(i)]), 2)

    result = result / 100
    UserInfo(name=request.user.username, test=result).save()
    return HttpResponseRedirect(reverse('profile'))


def submit_invite(request):
    user = request.GET['user']
    event = request.GET['event']
    r = int(request.GET['r'])
    Invite.objects.filter(name1=user, name2=request.user.username, event=event).update(submit=r)
    return HttpResponseRedirect(reverse('profile'))


def call(request):
    name1 = request.user.username
    name2 = request.POST['user_l']
    event_name = request.POST['event_l']
    event_id = Event.objects.get(name=event_name).id
    Invite(name1=name1, name2=name2, event=event_id, e_name=event_name, submit=False).save()
    return HttpResponseRedirect(reverse('profile'))


def add_event(request):
    global UPLOAD_FOLDER
    global ip
    try:
        name = request.POST['name']
        time = request.POST['time']
        text = request.POST['text']
        pic = request.FILES['photo']
        print(UPLOAD_FOLDER)
        with open(UPLOAD_FOLDER+pic.name, 'wb+') as destination:
            print(2)
            for chunk in pic.chunks():
                destination.write(chunk)

        Event(name=name, time=time, text=text, picture="http://"+ip+":8000/static/img/events/"+pic.name).save()
        return HttpResponseRedirect(reverse('events'))
    except:
        return render(request, 'add_event.html', {})


def remove_event(request):
    id = request.GET['event']
    Event.objects.get(id=id).delete()
    return HttpResponseRedirect(reverse('events'))


def remove_comment(request, event_id):
    pass
