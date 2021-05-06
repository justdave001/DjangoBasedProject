from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView

from .forms import GamesCreateForm, gamesLocationCreateForm
from .models import gamesLocation


class GamesListView(LoginRequiredMixin, ListView):
    def get_queryset(self):
      return gamesLocation.objects.filter(owner=self.request.user)

class GamesDetailView(LoginRequiredMixin,DetailView):
    def get_queryset(self):
      return gamesLocation.objects.filter(owner=self.request.user)

class gamesCreateView(LoginRequiredMixin, CreateView):
    form_class = gamesLocationCreateForm
    login_url = '/login/'
    template_name = 'form.html'
    #success_url = '/games/'

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.owner = self.request.user
        instance.save()
        return super(gamesCreateView, self).form_valid(form)
    def get_context_data(self, *args, **kwargs):
        context = super(gamesCreateView, self).get_context_data(*args,**kwargs)
        context['title'] = 'Add Game'
        return context


class gameUpdateView(LoginRequiredMixin, UpdateView):
    form_class = gamesLocationCreateForm
    login_url = '/login/'
    template_name = 'games/detail-update.html'
    #success_url = '/games/'

    def gets_context_data(self, *args, **kwargs):
        context = super(gameUpdateView, self).get_context_data(*args, **kwargs)
        name = self.get_object().name
        context['title'] = 'Update Game: {name}'
        return context
    def get_queryset(self):
      return gamesLocation.objects.filter(owner=self.request.user)

