from django.db import models
from gallery.controllers import upload_to
from filebrowser.fields import FileBrowseField

class Album(models.Model):

    ALBUM_ROLE_CHOICES = (
    ('BA', 'Стандартное'),
    ('WE', 'Свадебное'),
    )

    title = models.CharField(max_length=150)
    pub_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to=upload_to)
    role = models.CharField(choices=ALBUM_ROLE_CHOICES, max_length=2, default='BASIC')
    def __unicode__(self):
        return self.title

class Photo(models.Model):
    title = models.CharField(max_length=150)
    pub_date = models.DateTimeField(auto_now_add=True)
    image = FileBrowseField("Image", max_length=200, directory="images/", extensions=[".jpg"], blank=True, null=True)
    album = models.ForeignKey(Album)

    def __unicode__(self):
        return self.title