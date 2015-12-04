from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^$', 'views.login'),
    url(r'^home/$', 'views.home'),
    url(r'^about/$', 'views.about'),
    url(r'^logout/$', 'views.logout'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^post/(?P<receiver>\d+)/(?P<name>.*)/$', 'views.send_post', name='send_post'),
    url(r'^post/$', 'views.view_my_post'),
    url(r'^post222/(?P<receiver>\d+)/(?P<name>.*)/$', 'views.send_post2', name='send_post2'),
]
