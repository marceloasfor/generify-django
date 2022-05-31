from drf_writable_nested import WritableNestedModelSerializer
from rest_framework import serializers

from generify.models import Song, Playlist, User


class SongSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Song
        fields = ['id', 'artist', 'name', 'file']


class PlaylistSerializer(WritableNestedModelSerializer, serializers.HyperlinkedModelSerializer):
    song = SongSerializer(many=True)
    class Meta:
        model = Playlist
        fields = ['id', 'name', 'cover', 'about', 'user_id', 'song']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        playlist = PlaylistSerializer()
        fields = ['id', 'username', 'password', 'email', 'birthdate']
