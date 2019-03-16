from django.shortcuts import render
from books.models import Book

# Create your views here.

def book_search(request):
    books = Book.objects.filter(title__icontains=request.GET['q'] )
    return render(request, "books.html", {"books":books})
    
    
