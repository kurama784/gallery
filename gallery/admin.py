from django.contrib import admin
from gallery.models import Album, Photo
class AlbumAdmin(admin.ModelAdmin):
        list_display = ['title']

class PhotoAdmin(admin.ModelAdmin):
        list_display = ['title']

admin.site.register(Album, AlbumAdmin)
admin.site.register(Photo, PhotoAdmin)