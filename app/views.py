# repositorios/views.py
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import RepositoryForm, NewUserForm
from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import Repository, User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)


class RepositoryListView(ListView):
    model = Repository
    template_name = "app/repository_list.html"
    context_object_name = "repositories"


class RepositoryDetailView(DetailView):
    model = Repository
    template_name = "app/repository_detail.html"
    context_object_name = "repository"


class RepositoryCreateView(CreateView):
    model = Repository
    form_class = RepositoryForm
    template_name = "app/repository_form.html"

    def get_success_url(self):
        return reverse_lazy("repository_detail", kwargs={"pk": self.object.pk})


class RepositoryUpdateView(UpdateView):
    model = Repository
    form_class = RepositoryForm
    template_name = "app/repository_form.html"

    def get_success_url(self):
        return reverse_lazy("repository_detail", kwargs={"pk": self.object.pk})


class RepositoryDeleteView(DeleteView):
    model = Repository
    template_name = "app/repository_confirm_delete.html"
    success_url = reverse_lazy("repository_list")


def register_user(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            messages.success(request, "Account created succesfully")
            return redirect("repository_list")
    else:
        form = NewUserForm()
    return render(request, "app/register.html", {"form": form})
