from django.db import models
from django.conf import settings
from books.models import Book

# Create your models here.
class Downloadable(models.Model):
   username = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
   downloadbook = models.ForeignKey(Book, on_delete=models.CASCADE)
    
def __str__(self):
    return self.title
    