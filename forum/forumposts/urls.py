from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.hello, name='hello'),
    url(r'^posts/$', views.view_posts, name='view posts'),
    url(r'^add/$', views.add_post, name='add posts'),
    url(r'^fake/$', views.fake_add, name='fake add'),
    url(r'^ajax/likepost/$', views.like_post, name='like post'),
    url(r'^post/(?P<pk>.+)$', views.view_comments, name='forumpost-detail'),
]
