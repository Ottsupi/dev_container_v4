from django.urls import path

from . import views

urlpatterns = [
    path('django/', views.django_index),
    path('drf/', views.drf_index.as_view()),
    path('list/', views.HelloListView.as_view()),
    path('detail/<int:id>/', views.HelloDetailsView.as_view())
]
