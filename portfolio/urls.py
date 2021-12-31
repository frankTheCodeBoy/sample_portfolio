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
    path(
        "book-app/",
        views.book_app,
        name="book_app",
    ),
    path(
        "learning-app/",
        views.learning_log,
        name="learning_log",
    ),
    path(
        "android-app/",
        views.android_project,
        name="android_project",
    ),
    path(
        "social-webapp/",
        views.social_site,
        name="social_site",
    ),
    path(
        "game-development/",
        views.game_dev,
        name="game_dev",
    ),
    path(
        "global-data/",
        views.global_data,
        name="global_data",
    ),
    path(
        "machine-analytics/",
        views.machine_analytics,
        name="machine_analytics",
    ),
    
]