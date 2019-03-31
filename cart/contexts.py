from django.shortcuts import get_object_or_404
from books.models import Book


def cart_contents(request):

        cart = request.session.get('cart', {})
    
        cart_items = []
        total = 0
        book_count = 0
        for id, quantity in cart.items():
            book = get_object_or_404(Book, pk=id)
            total += book.price
            book_count += quantity
            cart_items.append({'id':id, 'quantity': quantity, 'book': book})
            
        return { 'cart_items': cart_items, 'total': total, 'book_count': book_count }
    