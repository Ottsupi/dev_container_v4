from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.
def django_index(request):
    return HttpResponse("Hello, world!")

class drf_index(APIView):
    def get(self, request):
        return Response({"message": "Hello, World!"})
