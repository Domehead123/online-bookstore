from django.shortcuts import render
from .models import Downloadable


# Create your views here.

def view_downloads(request):
    downloads = Downloadable.objects.all()
    return render(request, "downloads.html", {'downloads': downloads})
    
    
    
    