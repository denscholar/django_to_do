from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("add_task/", views.add_task, name="add-task"),
    path("mark_as_complete/<int:pk>/", views.mark_as_complete, name="mark-as-complete"),
    path("mark_as_undone/<int:pk>/", views.mark_as_undone, name="mark-as-undone"),
]
