# repositorios_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.register_user, name="register"),
    path("", views.RepositoryListView.as_view(), name="repository_list"),
    path("new/", views.RepositoryCreateView.as_view(), name="repository_create"),
    path("<int:pk>/", views.RepositoryDetailView.as_view(), name="repository_detail"),
    path(
        "<int:pk>/edit/", views.RepositoryUpdateView.as_view(), name="repository_update"
    ),
    path(
        "<int:pk>/delete/",
        views.RepositoryDeleteView.as_view(),
        name="repository_delete",
    ),
]
