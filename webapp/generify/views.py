from django.http import HttpResponse
from django.views import View
from rest_framework import viewsets
from rest_framework import permissions

from generify.models import Song, Playlist, User
from generify.serializers import (
    SongSerializer,
    PlaylistSerializer,
    UserSerializer,
)


class SongViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows songs to be viewed or edited.
    """
    queryset = Song.objects.all().order_by('id')
    serializer_class = SongSerializer
    permission_classes = [permissions.AllowAny]
    
    def get_queryset(self):
        qs = self.queryset
        name = self.request.query_params.get('name')
        if name:
            qs = Song.objects.filter(name__icontains=name).order_by('id')
        return qs


class PlaylistViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows playlists to be viewed or edited.
    """
    queryset = Playlist.objects.all().order_by('id')
    serializer_class = PlaylistSerializer
    permission_classes = [permissions.AllowAny]


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


class CoverView(View):
    model = Playlist

    def get(self, request, *args, **kwargs):
        playlist_id = kwargs.get('id')
        cover = self.model.objects.get(id=playlist_id)
        return HttpResponse(cover.cover, content_type='image/png')
