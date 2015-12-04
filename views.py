from django.shortcuts import render_to_response, redirect, render
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.template import Context

from helper.facebookAPI import fb_api_request
from helper.postHelper import post_tracker, post_retriever

from Sanare.models import LovePost, MatchedPair


def login(request):
    if request.flavour == 'mobile':
        return render(request, 'mobile_redirection_page.html')
    else:
        return render(request, 'login.html')


def about(request):
    return render(request, 'about.html')


@login_required(login_url='/')
def home(request):
    social_user = request.user.social_auth.filter(provider='facebook', ).first()
    info_list = []
    if social_user:
        info_list = fb_api_request.get_friends_info_list(social_user)
    context = Context({"info": info_list, "user": request.user})
    return render(request, "home.html", context)


@login_required(login_url='/')
def send_post(request, receiver, name):
    social_user = request.user.social_auth.filter(provider='facebook', ).first()
    info_list = []
    if social_user:
        info_list = fb_api_request.get_friends_info_list(social_user)
    that_info = []
    for info in info_list:
        if receiver == info[3]:
            that_info.append(info)
            break
    context = Context({"each_info": that_info[0], "user": request.user})
    return render(request, "confirm_sending.html", context)


def logout(request):
    auth_logout(request)
    return redirect('/')


@login_required(login_url='/')
def view_my_post(request):
    social_user = request.user.social_auth.filter(provider='facebook', ).first()
    uid = social_user.uid
    matches = post_retriever.get_all_matches(uid)
    posts = LovePost.objects.all().filter(sender_id=uid)
    for post in posts:
        if post_tracker.is_post_old(post):
            post.is_old = True
    context = Context({"posts": posts, "user": request.user, "matches": matches})
    return render_to_response("my_posts.html", context)


@login_required(login_url='/')
def send_post2(request, receiver, name):
    social_user = request.user.social_auth.filter(provider='facebook', ).first()
    uid = social_user.uid
    posts = LovePost.objects.all().filter(sender_id=uid)
    matches = post_retriever.get_all_matches(uid)
    for post in posts:
        if post_tracker.is_post_old(post):
            post.is_old = True
            post.save()
    new_post = LovePost(sender_id=uid, receiver_id=receiver, sender_name=request.user.get_username(), receiver_name=name)
    if post_tracker.cannot_send(new_post):
        posts = post_retriever.get_all_posts(uid)
        error_messages = ["You have sent a post recently!"]
        context = Context({"posts": posts, "error_messages": error_messages, "user": request.user, "matches": matches})
        return render(request, "my_posts.html", context)
    new_post.save()
    if post_tracker.matched(new_post):
        posts = post_retriever.get_all_posts(uid)
        new_matched_pair = MatchedPair(id1=new_post.sender_id, id2=new_post.receiver_id, name1=request.user.get_username(), name2=name)
        new_matched_pair.save()
        context = Context({'matched': new_matched_pair,"posts": posts, "user": request.user, "matches": matches})
        return render(request, "my_posts.html", context)
    return redirect('/post')
