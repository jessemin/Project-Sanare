import urllib2
import json


def create_friends_api_request(social_user):
    url = u'https://graph.facebook.com/{0}/' \
          u'friends?fields=id,name,email,picture.width(320).height(320)&limit=5000' \
          u'&access_token={1}'.format(
        social_user.uid,
        social_user.extra_data['access_token'],
    )
    request = urllib2.Request(url)
    return request


def get_friends_info_list(social_user):
    request = create_friends_api_request(social_user)
    friends = json.loads(urllib2.urlopen(request).read()).get('data')
    info_list = []
    count = 0
    for friend in friends:
        name = friend['name']
        uid = friend['id']
        image = friend['picture']['data']['url']
        info_tuple = (name, image, count, uid)
        info_list.append(info_tuple)
        count += 1
    return info_list


def get_image(uid):
    url = u'https://graph.facebook.com/{0}/' \
          u'picture'.format(uid)
    request = urllib2.Request(url)
    picture = urllib2.urlopen(request).read()
    return picture
