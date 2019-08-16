from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import generic

from authorization.forms import LoginForm


class LoginFormView(generic.View):
    form_class = LoginForm
    template = 'authorization/login.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect(reverse('home'))
        return render(request, self.template, {'form', form})


class LogoutView(generic.View):
    def get(self, request):
        logout(request)
        return redirect(reverse('home'))
