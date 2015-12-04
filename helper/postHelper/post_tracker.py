import datetime
from django.utils.timezone import utc
from Sanare.models import LovePost


def is_post_old(post):
    now = datetime.datetime.utcnow().replace(tzinfo=utc)
    dt = now - post.pub_date
    return dt.days >= 3


def cannot_send(post):
    uid = post.sender_id
    posts = LovePost.objects.all().filter(sender_id=uid, is_old=False)
    if len(posts) > 0:
        return True
    else:
        return False


def matched(post):
    uid = post.sender_id
    received_posts = LovePost.objects.all().filter(receiver_id=uid, is_old=False)
    for received_post in received_posts:
        if received_post.sender_id == post.receiver_id:
            return True
    return False

