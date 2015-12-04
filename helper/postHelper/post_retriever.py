from Sanare.models import LovePost, MatchedPair
import post_tracker


def get_all_posts(uid):
    posts = LovePost.objects.all().filter(sender_id=uid)
    for post in posts:
        if post_tracker.is_post_old(post):
            post.is_old = True
    return posts


def get_all_matches(uid):
    matches = MatchedPair.objects.all().filter(id1=uid) | MatchedPair.objects.all().filter(id2=uid)
    return matches
