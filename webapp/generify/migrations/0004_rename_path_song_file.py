# Generated by Django 4.0.4 on 2022-05-22 22:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('generify', '0003_alter_user_playlist'),
    ]

    operations = [
        migrations.RenameField(
            model_name='song',
            old_name='path',
            new_name='file',
        ),
    ]
