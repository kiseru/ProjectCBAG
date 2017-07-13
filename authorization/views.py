from django.contrib.auth import authenticate, login, logout
from django.http import Http404, HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
def log_in(request):
    if request.method == 'GET':
        return render(request, 'authorization/log_in.html')
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
        return redirect('/')
    else:
        return Http404()


def log_out(request):
    logout(request)
    return redirect(request, '')
