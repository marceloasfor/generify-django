from django.contrib import admin
from django.urls import reverse
from django.utils.safestring import mark_safe

from generify.models import Song, Playlist, User


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'artist')
    ordering = ('id',)


@admin.register(Playlist)
class PlaylistAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    readonly_fields = ('cover_preview',)

    def cover_preview(self, obj):
        if obj.id:
            return mark_safe('<img src="{}"/>'.format(
                reverse('generify:cover', args=(obj.id,)),
            ))
    
    cover_preview.short_description = 'Foto de Capa'
    cover_preview.allow_tags = True



@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email')
