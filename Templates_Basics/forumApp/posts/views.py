from datetime import datetime

from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect

from posts.models import Department


def homework_view(request):

    context = {
        "full_name": "John Doe",
        "address": "New York",
        "departments": Department.objects.values_list("name", flat=True).order_by("id"),
    }

    return render(request, 'homework.html', context)


def homework_id_view(request, pk):
    try:
        department = Department.objects.get(id=pk)
    except Department.DoesNotExist:
        return HttpResponseNotFound('<h1>Sorry, Department does not exist</h1>')

    context = {
        "name": department.name,
        "date": department.date,
        "description": department.description,
    }
    return render(request, 'department.html', context)


def index(request):
    return HttpResponse("<h1>Hello, world. You're at the Home view page.</h1>")


def dashboard(request):

    context = {
        "posts": [
            {
                "title": "New Down",
                "author": "John Doe",
                "content": "This is my first post!",
                "created_at": datetime.now()
            },
            {
                "title": "Hollywood Story",
                "author": "Michael Smith",
                "content": "This is my second post!",
                "created_at": datetime.now()
            },
            {
                "title": "American Crime",
                "author": "",
                "content": "This is my third post!",
                "created_at": datetime.now()
            },
        ],
    }

    return render(request, 'base.html', context)
