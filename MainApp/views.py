from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404, HttpResponseNotFound
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from MainApp.forms import SnippetForm


def index_page(request):
    context = {'pagename': 'PythonBin'}
    return render(request, 'pages/index.html', context)


def add_snippet_page(request):
    if request.method == "GET":
        form = SnippetForm()
        context = {
            'pagename': 'Добавление нового сниппета',
            'form': form
        }
        return render(request, 'pages/add_snippet.html', context)
    if request.method == "POST":
        form = SnippetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list")
        return render(request, 'add_snippet.html', {'form': form})


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


def delete_snippet(request, id_snip):
    snippet = get_object_or_404(Snippet, id=id_snip)

    if request.method == "POST":
        snippet.delete()
        return redirect('list')


def update_snippet(request, id_snip):
    snippet = get_object_or_404(Snippet, id=id_snip)
    # submitbutton = request.POST.get("submit")

    if request.method == "POST":
        form = SnippetForm(request.POST)
        if form.is_valid():
            snippet.name = form["name"].value()
            snippet.lang = form["lang"].value()
            snippet.code = form["code"].value()
            snippet.save()
            return redirect("list")
        return render(request, 'pages/update.html',
                      {'form': form, 'name': form["name"].value()})

