from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import StoryList, StroyDetail, ResponseList, ResponseDetail, StoryResponseList
#from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    url(r'^api/story/$', StoryList.as_view()),
    url(r'^api/story/(?P<pk>[0-9]+)$', StroyDetail.as_view()),
    url(r'^api/response/$', ResponseList.as_view()),
    url(r'^api/response/(?P<pk>[0-9]+)$', ResponseDetail.as_view()),
    url(r'^api/responses/(?P<storyId>.+)/$', StoryResponseList.as_view()),

]
