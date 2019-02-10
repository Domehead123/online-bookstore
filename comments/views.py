from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required
from books.models import Book
from books.views import book_details
from.forms import AddCommentForm
from django.http import HttpResponse, HttpResponseRedirect

@login_required    
def add_comment(request, pk):
    comment=None
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        form = AddCommentForm(request.POST, request.FILES, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.username = request.user
            comment.book = book
            comment = form.save()
            next = request.POST.get('next', '/')
            return HttpResponseRedirect(next)
    else:
        form = AddCommentForm(instance=comment)
        return render(request, 'add-comment.html', {'form': form})
    
    
    