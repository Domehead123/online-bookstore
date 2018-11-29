from django.test import TestCase

from .models import Book

# Create your tests here.
class BookTests(TestCase):
    
    def test_str(self):
        test_title = Book(title='Example book')
        self. assertEqual(str(test_title), 'Example book')