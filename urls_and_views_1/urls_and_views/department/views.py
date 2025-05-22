from datetime import datetime

from django.http import HttpResponse, Http404
from django.shortcuts import render

from department.models import Department


def home_page(request):
    return HttpResponse('<h1>Hello World! This is Home Page</h1>')


def department_page(request):
    departments = Department.objects.all()
    return HttpResponse(departments)


def show_department_by_id(request, department_id):
    try:
        department = Department.objects.get(pk=department_id)
        return HttpResponse(f"<h1>Hello from {department.name} with ID: {department_id}</h1>")
    except Department.DoesNotExist:
        return render(request, 'departments/search_by_name.html')


def show_department_by_name(request, department_name):
        try:
            department = Department.objects.get(name=department_name)
            return HttpResponse(f'<h1>Hello from {department.name}</h1>')
        except Department.DoesNotExist:
            raise Http404


def show_department_by_slug(request, department_slug):
    try:
        department = Department.objects.get(slug=department_slug)
        return HttpResponse(f'<h1>Hello from {department.name}</h1>')
    except Department.DoesNotExist:
        return HttpResponse(f'<h1>Sorry There is no Department with slug: {department_slug}</h1>')


def show_departments_by_year(request, year):
    year_date = datetime.strptime(year, "%Y-%m-%d").date()
    departments = Department.objects.get(year=year_date)
    return HttpResponse(f"<h1>This Department is from {departments.year}</h1>")

