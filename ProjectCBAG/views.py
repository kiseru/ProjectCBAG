from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse


@login_required()
def home(request):
    user = request.user

    context = {
        'first_name': user.first_name,
        'last_name': user.last_name,
        'group': ''
    }

    if context['group'] == 'Starostas':
        return redirect(reverse('groups:students'))
    elif context['group'] == 'Jury':
        return redirect(reverse('groups:jury'))

    return render(request, 'home.html', context)
