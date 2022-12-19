from django.http.response import Http404,HttpResponseRedirect
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.urls import resolve, reverse
from django.contrib.auth import authenticate

from watch_demo.apps.account.models import User

@login_required(login_url='accounts/login')
def index(request):
    user = request.user
    print(user.username)
    return render(request, 'index.html', {})



def user_login(request):
    if request.method == 'GET':
        return render(request, 'login.html', {})
    elif request.method == 'POST':
        username = request.POST.get('username', None)
        passwork = request.POST.get("password", None)
        user = authenticate(username=username, password=passwork)
        if user is not None:
            # A backend authenticated the credentials
            # print("sbbbbbbbbbbbbbbbbbbbbbb")
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            # No backend authenticated the credentials
            return 
            # return render(request, 'login.html', {})
        
    else:
        return Http404
    

def jump_sso(request):
    ...