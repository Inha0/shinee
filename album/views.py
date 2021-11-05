from django.shortcuts import render
from .models import Album

# Create your views here.
def index(request):
    album = Album.objects.all()
    context = {
        "al" : album,
    }
    return render (request, "album/index.html", context)