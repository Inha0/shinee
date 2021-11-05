from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import User

# Create your views here.
def index(request):
    return render (request, "main/index.html")

def userlogin(request):
    if request.method == "POST":
        un = request.POST.get("username")
        pw = request.POST.get("password")
        user = authenticate(username=un, password=pw)
        if user:
            login(request, user)
        else:
            messages.info(request, '로그인에 실패했습니다.')
            return redirect("main:userlogin")
        return redirect('main:index')
    return render (request, "main/userlogin.html")

def userlogout(request):
    logout(request)
    return redirect('main:index')

def signup(request):
    if request.method == "POST":
        if request.POST['password'] == request.POST['repassword']:
            un = request.POST.get("username")
            pw = request.POST.get("password")
            nn = request.POST.get("username")
            User.objects.create_user(username=un, password=pw, nickname=nn)
            return redirect("main:index")
        else:
            messages.info(request, '비밀번호가 일치하지 않습니다.')
    return render(request, "main/signup.html")

def userdel(request):
    u = User.objects.get(username=request.user.username)
    u.delete()
    return redirect("main:index")

def usermod(request):
    if request.method == "POST":
        un = request.user.username
        u = User.objects.get(username=un)
        ni = request.POST.get("nickname")
        co = request.POST.get("comment")
        pi = request.FILES.get("pic")
        u.nickname = ni
        u.comment = co
        if pi:
            u.pic = pi
        u.save()
        user = authenticate(username=un)
        login(request, user)
        return redirect('main:index')

    return render(request, "main/usermod.html")

def usermod2(request):
    if request.method == "POST":
        un = request.user.username
        u = User.objects.get(username=un)
        pw = request.POST.get("password")
        if pw:
            if request.POST['password'] == request.POST['repassword']:
                u.set_password(pw)
                u.save()
                user = authenticate(username=un, password=pw)
                login(request, user)
                return redirect('main:index')
            else:
                messages.info(request, '비밀번호가 일치하지 않습니다.')
        else:
            messages.info(request, '재설정할 비밀번호를 입력하지 않았습니다.')
    return render(request, "main/usermod2.html")