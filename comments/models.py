from django.db import models
from django.conf import settings
from books.models import Book
from django import forms

# Create your models here.
class Comment(models.Model):
   username = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
   book = models.ForeignKey(Book, on_delete=models.CASCADE)
   comment = models.TextField()
    
def __str__(self):
    return self.title

