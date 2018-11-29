from django.conf.urls import url, include
from .views import all_books, book_details


urlpatterns = [
    url(r'^$', all_books, name='books'),
    url(r'^(?P<pk>\d+)/$', book_details, name='book-details')
    ]
    
    
    