from django.http import HttpResponse
from rest_framework import generics, mixins, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import HelloMessages
from .serializers import HelloReadSerializer, HelloReadViewSetSerializer, HelloWriteSerializer


# Create your views here.
def django_index():
    return HttpResponse('Hello, world!')


class DRFIndex(APIView):
    def get(self):
        return Response({'message': 'Hello, World!'})


class HelloListView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = HelloMessages.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'PUT':
            return HelloWriteSerializer
        return HelloReadSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class HelloDetailsView(
    mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView
):
    queryset = HelloMessages.objects.all()
    lookup_field = 'id'

    def get_serializer_class(self):
        if self.request.method == 'PUT':
            return HelloWriteSerializer
        return HelloReadSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class HelloMessagesViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = HelloMessages.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return HelloWriteSerializer
        return HelloReadViewSetSerializer


class HelloMessageDetailViewSet(
    viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin
):
    queryset = HelloMessages.objects.all()
    lookup_field = 'id'

    def get_serializer_class(self):
        if self.request.method in ('PUT', 'PATCH'):
            return HelloWriteSerializer
        return HelloReadViewSetSerializer
