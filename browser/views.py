from django.shortcuts import render

from django.http import HttpResponse, JsonResponse
from django.template import RequestContext, loader

from django.contrib.auth.decorators import login_required

import os

from browser.lib import files


# Create your views here.
def get_path(request):
    if "path" in request.GET:
        return request.GET["path"]
    else:
        return files.BASE

@login_required(login_url='/admin/')
def index(request):
    context = {
        "files": files.list(get_path(request)),
    }
    return render(request, 'browser/index.html', context)

@login_required(login_url='/admin/')
def open(request):
    context = {
        "content": files.load(get_path(request))
    }
    return render(request, 'browser/view.html', context)

@login_required(login_url='/admin/')
def list_files(request):
    path = request.GET["path"]
    file_list = files.list(path)
    return JsonResponse(file_list, safe=False)
