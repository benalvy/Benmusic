
from django.contrib import admin

from playlist.models import Album, Artist, Song, info, source

# Register your models here
admin.site.register(info)
admin.site.register(source)
admin.site.register(Artist)
admin.site.register(Album)
admin.site.register(Song)
