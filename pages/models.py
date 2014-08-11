from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    place = models.CharField(max_length=50)
    content = models.TextField(max_length=500)