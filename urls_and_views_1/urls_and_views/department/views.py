from datetime import datetime

from django.http import HttpResponse, Http404
from django.shortcuts import render

from department.models import Department


def home_page(request):
    return render(request, 'departments/show_department.html')


def show_department_by_id(request, id):
    try:
        department = Department.objects.get(id=id)
        return HttpResponse(f"<h1>Hello from Department {department.id}</h1>")
    except Department.DoesNotExist:
        raise Http404


def show_department_by_name(request, name):
    department = Department.objects.get(name=name)
    return HttpResponse(f"<h1>Hello from Department {department.name}</h1>")


def show_department_by_slug(request, slug):
    department = Department.objects.get(slug=slug)
    return HttpResponse(f"<h1>Hello from Department {department.name}</h1>")


def show_departments_by_year(request, year):
    year_date = datetime.strptime(year, "%Y-%m-%d").date()
    departments = Department.objects.get(year=year_date)
    return HttpResponse(f"<h1>This Department is from {departments.year}</h1>")


def search_department_by_name(request, name):
    department = Department.objects.filter(name=name)
    context = {"department": department}

    return render(request, 'departments/search_by_name.html', context)
