from django.urls import path

from notes import views
from notes.views import IndexListView, NotesCreateView, NotesUpdateView, NotesDeleteView

urlpatterns = [
    # path("", views.index, name="index"),
    path("", IndexListView.as_view(), name="index"),
    path("create/", NotesCreateView.as_view(), name="create_notes"),
    path("update/<int:pk>", NotesUpdateView.as_view(), name="update_notes"),
    path("delete/<int:pk>", NotesDeleteView.as_view(), name="delete_notes"),

]