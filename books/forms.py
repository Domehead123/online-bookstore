from django import forms
from .models import Book

data = {'username': 'fish'}

class AddBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'author', 'genre', 'description', 'excerpt', 'price', 'file')
        exclude = ('username',)
        
        
        
      

        