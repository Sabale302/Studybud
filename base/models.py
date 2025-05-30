from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Topic(models.Model):
    name = models.CharField( max_length=200 )

    def __str__(self):
        return self.name


class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    participants = models.ManyToManyField(User, related_name='participants', blank=True)
    name = models.CharField( max_length=200 )
    description = models.TextField( null=True )
    created = models.DateTimeField( auto_now_add=True )
    updated = models.DateTimeField( auto_now=True )

    class Meta:
        ordering = ['-updated','-created']

    def __str__(self):
        return self.name
    
class Message(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField( auto_now_add=True )
    updated = models.DateTimeField( auto_now=True )

    class Meta:
        ordering = ['-updated','-created']

    def __str__(self):
        return self.body[:50]