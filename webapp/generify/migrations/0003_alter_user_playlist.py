# Generated by Django 4.0.4 on 2022-05-20 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generify', '0002_remove_playlist_song_playlist_song_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='playlist',
            field=models.ManyToManyField(blank=True, to='generify.playlist'),
        ),
    ]
