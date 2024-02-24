from django.http import HttpResponse
from django.shortcuts import render
from hello.models import HelloMessage
from hello.serializers import HelloReadSerializer, HelloWriteSerializer
from rest_framework import generics, mixins, serializers, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.
def index(request):
    '''
    Hello world! view for base Django
    '''
    test = 1 + 1
    test = test ** 4
    return HttpResponse('Hello world! <br> --from django')


class DrfIndex(APIView):
    '''
    Hello world! view for Django Rest Framework
    '''
    serializer_class = serializers.Serializer

    def get(self, request):
        return Response({
            'message' : 'Hello world!',
            'from' : 'Django Rest Framework'
        })


class HelloListCreateView(mixins.ListModelMixin,
                          mixins.CreateModelMixin,
                          generics.GenericAPIView):
    queryset = HelloMessage.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return HelloReadSerializer
        if self.request.method == 'POST':
            return HelloWriteSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class HelloDetailView(mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin,
                      generics.GenericAPIView):
    queryset = HelloMessage.objects.all()
    lookup_field = 'id'

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return HelloReadSerializer
        if self.request.method == 'PUT':
            return HelloWriteSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


# Viewsets


class HelloViewSet(viewsets.GenericViewSet,
                       mixins.ListModelMixin,
                       mixins.CreateModelMixin):
    queryset = HelloMessage.objects.all()
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return HelloReadSerializer
        if self.request.method == 'POST':
            return HelloWriteSerializer


class HelloDetailViewSet(viewsets.GenericViewSet,
                         mixins.RetrieveModelMixin,
                         mixins.UpdateModelMixin,
                         mixins.DestroyModelMixin):
    queryset = HelloMessage.objects.all()
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return HelloReadSerializer
        return HelloWriteSerializer
