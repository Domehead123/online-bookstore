from django.db import models
from django.conf import settings



# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=300, default='')
    author = models.CharField(max_length=300, default='')
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
    )
    description = models.TextField()
    excerpt = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    file = models.FileField()
    username = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)



    
    def __str__(self):
        return self.title