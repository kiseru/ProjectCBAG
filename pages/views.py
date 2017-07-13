from django.shortcuts import render, redirect


def home(request):
    user = request.user
    if user.is_authenticated:
        context = {
            'first_name': user.first_name,
            'last_name': user.last_name,
        }

        return render(request, 'pages/home.html', context)
    else:
        return redirect('/auth/log_in')
