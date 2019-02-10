from django.conf.urls import url
from .views import view_downloads

urlpatterns = [
    url(r'^$', view_downloads, name='view_downloads')]
    
    
    
    