from rest_framework import generics, permissions, status
from .serializers import StorySerializer, ResponseSerializer
from .models import Story, Response


#from django.contrib.auth.models import User
from django.shortcuts import render
#from rest_framework.response import Response
#from rest_framework.views import APIView




class StoryList(generics.ListCreateAPIView):
    serializer_class = StorySerializer

    def get_queryset(self):
#        tech = self.kwargs['tech']
        return Story.objects.filter(approved=True)

class StroyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Story.objects.all()
    serializer_class = StorySerializer


class ResponseList(generics.ListCreateAPIView):
    serializer_class = ResponseSerializer

    def get_queryset(self):
#        tech = self.kwargs['tech']
        return Response.objects.filter(approved=True)

class ResponseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Response.objects.all()
    serializer_class = ResponseSerializer




