# Generated by Django 4.0.4 on 2022-05-23 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generify', '0004_rename_path_song_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playlist',
            name='cover',
            field=models.ImageField(default='rock.jpg', help_text='Capa da playlist.', upload_to=''),
        ),
    ]