from django.db.models import Q
from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect
from posts.models import Department, Post
from posts.forms import PostCreateForm, PostEditForm, PostDeleteForm, SearchForm


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

        return render(request, "posts/dashboard.html", context)


def add_post(request):
    form = PostCreateForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('dashboard')

    context = {
        "form": form,
    }

    return render(request, 'posts/add-post.html', context)


def edit_post(request, pk: int):
    post = Post.objects.get(pk=pk)
    form = PostEditForm(request.POST or None, instance=post)  # instance=post -> Ще презареди с попълнени данни!

    if request.method == "Post" and form.is_valid():
        form.save()
        return redirect('dashboard')

    context = {
        "form": form,
    }

    return render(request, 'posts/edit-post.html', context)


def post_details(request, pk: int):
    post = Post.objects.get(pk=pk)

    context = {
        "post": post,
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
