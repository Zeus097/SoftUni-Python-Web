from datetime import datetime
from dataclasses import fields

from django.db.models import Q
from django.forms import modelform_factory
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, RedirectView, CreateView, UpdateView, DeleteView, FormView

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


class CreateDepartment(CreateView):
    model = Department
    form_class = CreateDepartmentForm
    success_url = reverse_lazy('departments')

    template_name = 'department/add_department.html'


# def add_department_view(request):
#     form = CreateDepartmentForm(request.POST or None, request.FILES or None)
#
#     if request.method == 'POST' and form.is_valid():
#         form.save()
#         return redirect('departments')
#
#     context = {
#         'form': form
#     }
#
#     return render(request, 'department/add_department.html', context)


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


class DeleteDepartment(DeleteView, FormView):
    model = Department
    form_class = DeleteDepartmentForm
    template_name = 'department/delete_department.html'
    success_url = reverse_lazy('departments')

    def get_initial(self):
        pk = self.kwargs.get(self.pk_url_kwarg)
        department = self.model.objects.get(pk=pk)
        return department.__dict__


# def delete_department_view(request, pk):
#     department = Department.objects.get(pk=pk)
#     form = DeleteDepartmentForm(instance=department)
#
#     if request.method == 'POST':
#         department.delete()
#         return redirect('departments')
#
#     context = {
#         'form': form,
#         'department': department
#     }
#
#     return render(request, 'department/delete_department.html', context)


def department_details_view(request, pk):
    department = Department.objects.get(id=pk)

    context = {
        'department': department
    }

    return render(request, 'department/department_details.html', context)










def index(request):
    return render(request, 'index.html')

# Simple example of Django under the hood
# class MyView:
#
#     def dispatch(self, request, *args, **kwargs):
#         if request.method == "GET":
#             return self.get(request, *args, **kwargs)
#         ...
#
#     @classonlymethod
#     def as_view(cls):
#
#         def view(request, *args, **kwargs):
#             self = cls()
#             return self.dispatch(request, args, kwargs)
#
#         return view


class IndexView(TemplateView):
    # template_name = 'index.html'  # static way
    # extra_context = {  # static way
    #     "current_time": datetime.now(),
    # }

    def get_context_data(self, **kwargs):
        super().get_context_data(**kwargs)
        kwargs.update({  # dynamic way
            "current_time": datetime.now(),
        })
        return kwargs

    def get_template_names(self):  # dynamic way
        if self.request.user.is_superuser:
            return ['index_for_admin.html']

        return ['jhfqwkandoixeu', 'index.html']


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


class CreatePost(CreateView):
    model = Post
    form_class = PostCreateForm
    success_url = reverse_lazy('dashboard')
    template_name = 'posts/add-post.html'


# def add_post(request):
#     form = PostCreateForm(request.POST or None, request.FILES or None)
#
#     if request.method == "POST" and form.is_valid():
#         form.save()
#         return redirect('dashboard')
#
#     context = {
#         "form": form,
#     }
#
#     return render(request, 'posts/add-post.html', context)


class EditPost(UpdateView):
    model = Post
    success_url = reverse_lazy('dashboard')
    template_name = 'posts/edit-post.html'

    def get_form_class(self):
        if self.request.user.is_superuser:
            return modelform_factory(Post, fields='__all__')
        else:
            return modelform_factory(Post, fields=['content'])


# def edit_post(request, pk: int):
#     post = Post.objects.get(pk=pk)
#
#     if request.user.is_superuser:
#         PostEditForm = modelform_factory(Post, fields='__all__')
#     else:
#         PostEditForm = modelform_factory(Post, fields=('content',),)
#
#     form = PostEditForm(request.POST or None, instance=post)
#
#     if request.method == "POST" and form.is_valid():
#         form.save()
#         return redirect('dashboard')
#
#     context = {
#         "form": form,
#     }
#
#     return render(request, 'posts/edit-post.html', context)


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


class DeletePost(DeleteView, FormView):
    model = Post
    form_class = PostDeleteForm
    template_name = 'posts/delete-post.html'
    success_url = reverse_lazy('dashboard')

    def get_initial(self):
        pk = self.kwargs.get(self.pk_url_kwarg)
        post = self.model.objects.get(pk=pk)
        return post.__dict__


# def delete_post(request, pk: int):
#     post = Post.objects.get(pk=pk)
#     form = PostDeleteForm(instance=post)
#
#     if request.method == "POST":
#         post.delete()
#         return redirect('dashboard')
#
#     context = {
#         "form": form,
#     }
#
#     return render(request, 'posts/delete-post.html', context)


class MyRedirectView(RedirectView):
    # url = 'http://localhost:8000/dashboard'
    # pattern_name = 'dashboard'
    # Both static ways

    def get_redirect_url(self, *args, **kwargs):  # dynamic way
        return reverse('dashboard') + "?query=Django"
