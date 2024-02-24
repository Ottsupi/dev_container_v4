from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views

urlpatterns = [
    path('django/', views.index),
    path('drf/', views.DrfIndex.as_view()),
    path('list/', views.HelloListCreateView.as_view()),
    path('<int:id>/detail', views.HelloDetailView.as_view(), name='hellomessage-detail')
]

router = DefaultRouter()
router.register(r'messages', views.HelloViewSet)
router.register(r'message', views.HelloDetailViewSet)

urlpatterns += router.urls
