from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404, HttpResponseNotFound
from django.shortcuts import render, redirect
from .models import *


def index_page(request):
    context = {'pagename': 'PythonBin'}
    return render(request, 'pages/index.html', context)


def add_snippet_page(request):
    context = {'pagename': 'Добавление нового сниппета'}
    return render(request, 'pages/add_snippet.html', context)


def snippets_page(request):
    snips = Snippet.objects.all()
    count = Snippet.objects.count()
    context = {'pagename': 'Просмотр сниппетов', 'snips': snips, 'count': count}
    return render(request, 'pages/view_snippets.html', context)


def snippet(request, id_snip):
    try:
        snip = Snippet.objects.get(id=id_snip)
    except ObjectDoesNotExist:
        return HttpResponseNotFound(f'Snippet with id={id_snip} not found')
    else:
        context = {
            "snip": snip,
        }
        return render(request, "pages/snippet.html", context)

