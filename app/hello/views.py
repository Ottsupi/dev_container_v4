from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import generics, mixins
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import HelloMessages
from .serializers import HelloMessagesSerializer


# Create your views here.
def django_index(request):
    return HttpResponse("Hello, world!")


class drf_index(APIView):
    def get(self, request):
        return Response({"message": "Hello, World!"})


class HelloListView(mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    generics.GenericAPIView):
    queryset = HelloMessages.objects.all()
    serializer_class = HelloMessagesSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class HelloDetailsView(mixins.RetrieveModelMixin,
                       mixins.UpdateModelMixin,
                       mixins.DestroyModelMixin,
                       generics.GenericAPIView):
    queryset = HelloMessages.objects.all()
    serializer_class = HelloMessagesSerializer
    lookup_field = 'id'

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
