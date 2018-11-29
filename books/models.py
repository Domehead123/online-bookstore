from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=300, default='')
    author = models.CharField(max_length=300, default='')
    genre = models.CharField(max_length=300, default='')
    description = models.TextField()
    excerpt = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    file = models.FileField()
    
    def __str__(self):
        return self.title