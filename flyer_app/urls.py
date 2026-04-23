from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("register/", views.register_view, name="register"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("profile/", views.profile_detail, name="profile_detail"),
    path("profile/edit/", views.profile_edit, name="profile_edit"),
    path("flyers/", views.flyer_list, name="flyer_list"),
    path("flyers/create/", views.flyer_create, name="flyer_create"),
    path("flyers/<int:pk>/", views.flyer_detail, name="flyer_detail"),
    path("flyers/<int:pk>/edit/", views.flyer_edit, name="flyer_edit"),
    path("flyers/<int:pk>/delete/", views.flyer_delete, name="flyer_delete"),
]