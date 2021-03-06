from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("complete-register/", views.complete_register, name="complete-register"),
    path("chat/<str:application_id>/",
         views.chat_with_employer, name="chat_with_employer"),
    path("zoom/callback/", views.zoom_callback, name="zoom_callback"),
    path("dashboard/", views.dashboard, name="dashboard"),
]
