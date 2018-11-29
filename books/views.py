from django.shortcuts import render, get_object_or_404
from .models import Book

# Create your views here.

def all_books(request):
    books = Book.objects.all()
    return render(request, "books.html", {"books": books})


def book_details(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, "book-details.html", {'book': book})