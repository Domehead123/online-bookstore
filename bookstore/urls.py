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
from books.views import all_books, book_details, edit_book, add_book
from django.views import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', all_books, name='books'),
    url(r'^(?P<pk>\d+)/$', book_details, name='book_details'),
    url(r'^accounts/', include(urls_accounts)),
    url(r'^add-book/$', add_book, name='add_book'),
    url(r'^(?P<pk>\d+)/edit/$',edit_book, name='edit_book')
]

