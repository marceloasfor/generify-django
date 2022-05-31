from django.db import models


class Song(models.Model):
    artist = models.CharField(max_length=150)
    name = models.CharField(max_length=150)
    file = models.URLField(
        help_text='URL of the song in the web',
        max_length=150,
    )

    def __str__(self):
        return self.name


class Playlist(models.Model):
    name = models.CharField(max_length=150)
    cover = models.ImageField(
        help_text='Capa da playlist.',
        default='rock.jpg',
    )
    about = models.CharField(
        help_text='Descrição visível para o usuário.',
        max_length=300,
    )
    song = models.ManyToManyField(Song)
    user_id = models.IntegerField(
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.name


class User(models.Model):
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=150)
    email = models.EmailField(max_length=254, unique=True)
    birthdate = models.DateField(blank=True)

    def __str__(self):
        return self.username
