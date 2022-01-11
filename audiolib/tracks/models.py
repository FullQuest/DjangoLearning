from django.db import models
import uuid

# Create your models here.


class Track(models.Model):
    title = models.CharField(max_length=200)
    author = models.ManyToManyField('Artist', blank=True)
    label = models.CharField(max_length=200, blank=True)
    description = models.TextField(null=True, blank=True)
    demo_link = models.CharField(max_length=2000, null=True, blank=True)
    genres = models.ManyToManyField('Genre', blank=True)
    added = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, 
                          primary_key=True, editable=False)

    def __str__(self):
        return f'{self.title}'


class Artist(models.Model):
    pseudonym = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200, blank=True)
    second_name = models.CharField(max_length=200, blank=True)
    third_name = models.CharField(max_length=200, blank=True)
    date_of_birth = models.DateField(blank=True, null=True)
    bio = models.CharField(max_length=5000, blank=True)
    added = models.DateTimeField(auto_now_add=True)
    tracks = models.ManyToManyField('Track', blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, 
                          primary_key=True, editable=False)

    def __str__(self):
        return f'{self.pseudonym}'


class Genre(models.Model):
    title = models.CharField(max_length=200)
    added = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, 
                          primary_key=True, editable=False)

    def __str__(self):
        return f'{self.title}'

