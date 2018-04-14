from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import StoryList, StoryDetail, ResponseList, ResponseDetail, StoryResponseList, BlogDetail, BlogList
#from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    url(r'^api/story/$', StoryList.as_view()),
    url(r'^api/story/(?P<pk>[0-9]+)$', StoryDetail.as_view()),
    url(r'^api/blogs/$', BlogList.as_view()),
    url(r'^api/blogs/(?P<pk>[0-9]+)$', BlogDetail.as_view()),
    url(r'^api/response/$', ResponseList.as_view()),
    url(r'^api/response/(?P<pk>[0-9]+)$', ResponseDetail.as_view()),
    url(r'^api/responses/(?P<storyId>[0-9]+)/$', StoryResponseList.as_view())
]
