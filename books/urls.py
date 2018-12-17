from django.conf.urls import url, include
from .views import all_books, book_details, edit_book, add_book


urlpatterns = [
    url(r'^$', all_books, name='books'),
    url(r'^(?P<pk>/<d+)/$', book_details, name='book_details'),
    url(r'^add-book/$', add_book, name='add_book'),
    url(r'^(?P<pk>\d+)/edit/$',edit_book, name='edit_book')
]


 
