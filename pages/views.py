from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


@login_required(login_url='/auth/log_in')
def home(request):
    user = request.user

    context = {
        'first_name': user.first_name,
        'last_name': user.last_name,
    }

    return render(request, 'pages/home.html', context)
