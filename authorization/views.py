from django.contrib.auth import authenticate, login
from django.http import Http404, HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
def log_in(request):
    if request.method == 'GET':
        return render(request, 'authorization/login.html')
    elif request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=email, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect(request, '/')
            else:
                return redirect(request, '/login/')
    else:
        return Http404()
