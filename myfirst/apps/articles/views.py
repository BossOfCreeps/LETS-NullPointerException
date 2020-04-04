# request.user.username
from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from .models import Event, Comment, UserInfo, Invite
from django.urls import reverse
from django.contrib.auth.models import User


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
    user = request.user.username
    test = -1
    try:
        test = UserInfo.objects.get(name=user).test
    except:
        pass
    invites = Invite.objects.filter(name2=user)
    my_invites = Invite.objects.filter(name1=user, submit=2)
    test_users = UserInfo.objects.filter()
    users_list = list()
    for tu in test_users:
        if test + 0.1 > tu.test > test - 0.1 and tu.name != user:
            users_list.append(tu.name)

    print(users_list)
    return render(request, 'profile.html', {"u": user, "test": test, "invites": invites, "my_invites": my_invites, "test_users": users_list})


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
            print(i,int(request.POST['id_' + str(i)]),1)
        if not (i in extra_list) and not int(request.POST['id_' + str(i)]):
            result += 5
            print(i,int(request.POST['id_' + str(i)]),2)

    result = result / 100
    UserInfo(name=request.user.username, test=result).save()
    return HttpResponseRedirect(reverse('profile'))


def submit_invite(request):
    user = request.GET['user']
    event = request.GET['event']
    r = int(request.GET['r'])
    Invite.objects.filter(name1=user, name2=request.user.username, event=event).update(submit=r)
    return HttpResponseRedirect(reverse('profile'))
