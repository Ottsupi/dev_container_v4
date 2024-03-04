from django.urls import path
from rest_framework.routers import SimpleRouter

from . import views

router = SimpleRouter()

router.register(r'messages', views.HelloMessagesListViewSet)
router.register(r'message', views.HelloMessageDetailViewSet)

urlpatterns = [
    path('django/', views.django_index),
    path('drf/', views.DRFIndex.as_view()),
    path('list/', views.HelloListView.as_view()),
    path('<int:id>/detail/', views.HelloDetailsView.as_view(), name='hello-detail'),
]

urlpatterns += router.urls
