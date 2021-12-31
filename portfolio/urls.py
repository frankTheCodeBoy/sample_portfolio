"""Defines urls for portfolio"""
from django.urls import path
from . import views

app_name = "portfolio"
urlpatterns = [
    path(
        "",
        views.index,
        name="index",
    ),
    path(
        "about/",
        views.about,
        name="about",
    ),
    path(
        "projects/",
        views.projects,
        name="projects",
    ),
    path(
        "services/",
        views.services,
        name="services",
    ),
    path(
        "contact/",
        views.contact,
        name="contact",
    ),
    path(
        "api-project/",
        views.api_project,
        name="api_project",
    ),
    
]