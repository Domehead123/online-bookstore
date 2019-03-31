from django.db import models
from django.conf import settings

# -*- coding: utf-8 -*-

# Create your models here.

class Book(models.Model):
    title = models.CharField(verbose_name="Title *", max_length=300, default='')
    author = models.CharField(verbose_name="Author *", max_length=300, default='')
    no_genre = 'No Genre'
    comedy = "Comedy"
    crime="Crime/Thriller"
    factual="Factual"
    historical="Historical"
    horror = 'Horror'
    romance = 'Romance'
    sci_fi = 'Science Fiction/Fantasy'
    crime="Crime/Thriller"
    genre_choices = (
        (no_genre, 'No Genre'),
        (comedy, 'Comedy'),
        (crime, 'Crime/Thriller'),
        (factual, 'Factual'),
        (historical, 'Historical'),
        (horror, 'Horror'),
        (romance, 'Romance'),
        (sci_fi, 'Science Fiction/Fantasy'),
        (crime, 'Crime/Thriller')
        
    )
    genre = models.CharField(
        max_length=30,
        choices=genre_choices,
        default=no_genre,
        verbose_name="Genre *"
    )
    description = models.TextField(verbose_name="Brief description of novel (500 characters max) *", max_length=500)
    excerpt = models.TextField(verbose_name="Opening chapter/s *")
    price = models.DecimalField(verbose_name="Price (sterling) *", max_digits=6, decimal_places=2)
    file = models.FileField(verbose_name="Upload book document *")
    username = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)


    
    def __str__(self):
        return self.title