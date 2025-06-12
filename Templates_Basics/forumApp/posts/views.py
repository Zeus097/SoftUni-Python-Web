from dataclasses import fields

from django.db.models import Q
from django.forms import modelform_factory
from django.shortcuts import render, redirect

from posts.models import Post, Department
from posts.forms import PostCreateForm, PostEditForm, PostDeleteForm, SearchForm, CommentForm, CommentFormSet, \
    CreateDepartmentForm, EditDepartmentForm, SearchDepartmentForm, DeleteDepartmentForm


def list_of_departments_view(request):
    search_form = SearchDepartmentForm(request.GET)
    departments = Department.objects.all().order_by('-id')
    if request.method == "GET" and search_form.is_valid():
        query = search_form.cleaned_data.get('query')
        departments = departments.filter(name__icontains=query)

    context = {
        'search_form': search_form,
        'departments': departments,
    }

    return render(request, 'department/departments.html', context)


def add_department_view(request):
    form = CreateDepartmentForm(request.POST or None, request.FILES or None)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('departments')

    context = {
        'form': form
    }

    return render(request, 'department/add_department.html', context)


def edit_department_view(request, pk):
    department = Department.objects.get(pk=pk)

    if request.user.is_superuser:
        EditDepartmentForm = modelform_factory(Department, fields='__all__')
    else:
        EditDepartmentForm = modelform_factory(Department, fields=['description'])

    form = EditDepartmentForm(request.POST or None, instance=department)

    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('departments')

    context = {
        'form': form
    }

    return render(request, 'department/edit_department.html', context)


def delete_department_view(request, pk):
    department = Department.objects.get(pk=pk)
    form = DeleteDepartmentForm(instance=department)

    if request.method == 'POST':
        department.delete()
        return redirect('departments')

    context = {
        'form': form,
        'department': department
    }

    return render(request, 'department/delete_department.html', context)


def department_details_view(request, pk):
    department = Department.objects.get(id=pk)

    context = {
        'department': department
    }

    return render(request, 'department/department_details.html', context)










def index(request):
    return render(request, 'index.html')


def dashboard(request):
    search_form = SearchForm(request.GET)
    posts = Post.objects.all()

    if request.method == "GET" and search_form.is_valid():
        query = search_form.cleaned_data.get('query')
        posts = posts.filter(
            Q(title__icontains=query)
                |
            Q(content__icontains=query)
                |
            Q(author__icontains=query)
        )

    context = {
        "posts": posts,
        "search_form": search_form,
    }

    return render(request, 'posts/dashboard.html', context)


def add_post(request):
    form = PostCreateForm(request.POST or None, request.FILES or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('dashboard')

    context = {
        "form": form,
    }

    return render(request, 'posts/add-post.html', context)


def edit_post(request, pk: int):
    post = Post.objects.get(pk=pk)

    if request.user.is_superuser:
        PostEditForm = modelform_factory(Post, fields='__all__')
    else:
        PostEditForm = modelform_factory(Post, fields=('content',),)

    form = PostEditForm(request.POST or None, instance=post)

    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('dashboard')

    context = {
        "form": form,
    }

    return render(request, 'posts/edit-post.html', context)


def post_details(request, pk: int):
    post = Post.objects.get(pk=pk)
    comment_form_set = CommentFormSet(request.POST or None)

    if request.method == "POST" and comment_form_set.is_valid():
        for form in comment_form_set:
            comment = form.save(commit=False)
            comment.author = request.user.username
            comment.post = post
            comment.save()
            return redirect('post-details', pk=post.pk)

    context = {
        "post": post,
        "formset": comment_form_set,
    }

    return render(request, 'posts/post-details.html', context)


def delete_post(request, pk: int):
    post = Post.objects.get(pk=pk)
    form = PostDeleteForm(instance=post)

    if request.method == "POST":
        post.delete()
        return redirect('dashboard')

    context = {
        "form": form,
    }

    return render(request, 'posts/delete-post.html', context)
