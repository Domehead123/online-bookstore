from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from .forms import AddBookForm
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from comments.models import Comment
from comments.forms import Comment




# Create your views here.

def all_books(request):
    books = Book.objects.all()
    return render(request, "books.html", {"books": books})

def book_details(request, pk):
    book = get_object_or_404(Book,pk=pk)
    return render(request, "book-details.html", {'book': book})

@login_required    
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        form = AddBookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            book = form.save()
            return redirect(all_books)
    else:
        form = AddBookForm(instance=book)
    return render(request, 'add-book.html', {'form': form})
    
@login_required    
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book.delete()
    return redirect(all_books)
  
@login_required    
def add_book(request, pk=None):
    book = None
    if request.method == "POST":
        form = AddBookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            book = form.save(commit=False)
            book.username = request.user
            book.save()
            return redirect(all_books)
    else:
        form = AddBookForm(instance=book)
    return render(request, 'add-book.html', {'form': form})
    
@login_required    
def add_comment(request, pk):
    comment = None
    if request.method == "POST":
        form = AddCommentForm(request.POST, request.FILES, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.username = request.user
            comment.save()
            return redirect(all_books)
    else:
        form = AddCommentForm(instance=comment)
    return render(request, 'add-comment.html', {'form': form})