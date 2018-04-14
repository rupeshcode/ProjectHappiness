from rest_framework import generics, permissions, status
from .serializers import StorySerializer, ResponseSerializer, BlogSerializer
from .models import Story, Response, Blog

#from django.contrib.auth.models import User
from django.shortcuts import render
#from rest_framework.response import Response
#from rest_framework.views import APIView


class StoryList(generics.ListCreateAPIView):
    serializer_class = StorySerializer

    def get_queryset(self):
#        tech = self.kwargs['tech']
        return Story.objects.filter(isModerated=True)


class StoryDetail(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = StorySerializer

    def get_queryset(self):
        #        tech = self.kwargs['tech']
        return Story.objects.filter(isModerated=True)


class ResponseList(generics.ListCreateAPIView):
    serializer_class = ResponseSerializer

    def get_queryset(self):
#        tech = self.kwargs['tech']
        return Response.objects.filter(isModerated=True)


class ResponseDetail(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = ResponseSerializer

    def get_queryset(self):
        #        tech = self.kwargs['tech']
        return Response.objects.filter(isModerated=True)


class StoryResponseList(generics.ListCreateAPIView):
    serializer_class = ResponseSerializer

    def get_queryset(self):
        storyId = self.kwargs['story']
        return Response.objects.filter(storyId=storyId, isModerated=True)


class BlogList(generics.ListCreateAPIView):
    serializer_class = BlogSerializer

    def get_queryset(self):
#        tech = self.kwargs['tech']
        return Blog.objects


class BlogDetail(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = BlogSerializer

    def get_queryset(self):
        #        tech = self.kwargs['tech']
        return Blog.objects


