from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'songs', views.SongViewSet)
router.register(r'playlists', views.PlaylistViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('playlists/<int:id>/cover/', views.CoverView.as_view(), name='cover'),
]
