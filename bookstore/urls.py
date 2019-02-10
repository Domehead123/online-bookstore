"""bookstore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from accounts import urls as urls_accounts
from search import urls as urls_search
from checkout import urls as urls_checkout
from cart import urls as urls_cart
from books import urls as urls_book
from downloads import urls as urls_downloads
from books.views import all_books, book_details, edit_book, add_book, delete_book
from comments.views import add_comment

from django.views import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', all_books, name='all_books'),
    url(r'^(?P<pk>\d+)/$', book_details, name='book_details'),
    url(r'^accounts/', include(urls_accounts)),
    url(r'^checkout/', include(urls_checkout)),
    url(r'^downloads/', include(urls_downloads)),
    url(r'^cart/', include(urls_cart)),
    url(r'^add-book/$', add_book, name='add_book'),
    url(r'^(?P<pk>\d+)/edit/$',edit_book, name='edit_book'),
    url(r'^search/', include(urls_search)),
    url(r'^(?P<pk>\d+)/delete/$',delete_book, name='delete_book'),
    url(r'^(?P<pk>\d+)/comment/$',add_comment, name='add_comment')
   
]

