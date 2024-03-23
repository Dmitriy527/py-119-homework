from django.shortcuts import render

from django.http import HttpResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from notes.forms import NotesForm
from notes.models import Notes


def index(requests):
    return HttpResponse('Hello from Notes app.')


class IndexListView(ListView):
    model = Notes
    template_name = 'home_page.html'


class NotesCreateView(CreateView):
    form_class = NotesForm
    template_name = 'create_notes.html'


class NotesUpdateView(UpdateView):
    model = Notes
    fields = ("title", "text", "category")
    template_name = 'update_notes.html'
    queryset = Notes.objects.all()
    success_url = "/notes/"


class NotesDeleteView(DeleteView):
    model = Notes
    success_url = "/notes/"
