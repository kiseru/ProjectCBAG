from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.views import generic


class HomeView(
               generic.View):
    def get(self, request):
        group_name = request.user.groups.get().name
        if group_name == 'headman':
            return redirect(reverse('groups:academicgroup_detail', args=(request.user.academicgroup.pk,)))
        elif group_name == 'jury':
            return redirect(reverse('groups:jury'))
        else:
            return redirect(reverse('auth:logout'))
