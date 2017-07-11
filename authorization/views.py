from django.contrib.auth import authenticate, login
from django.http import Http404, HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
def log_in(request):
    if request.method == 'GET':
        return render(request, 'authorization/login.html')
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponse('Success')
        else:
            return HttpResponse('Fail')
    else:
        return Http404()
