from django.shortcuts import render, redirect

# Create your views here.
def key(request):
    return render (request, "artist/key.html")

def jonghyun(request):
    return render (request, "artist/jonghyun.html")

def taemin(request):
    return render (request, "artist/taemin.html")

def onew(request):
    return render (request, "artist/onew.html")

def minho(request):
    return render (request, "artist/minho.html")