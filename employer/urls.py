from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("new/", views.post_job, name="post_job"),
    path("jobs/", views.view_all_jobs, name="view_all_jobs"),
    path("applications/", views.view_all_application,
         name="view_all_application"),
    path("application/<str:id>/", views.view_application, name="view_application"),
    path(
        "chat/<str:application_id>/",
        views.chat_with_candidate,
        name="chat_with_candidate",
    ),
    path("reject/<str:id>/", views.reject_candidate, name="reject_candidate"),
    path("hire/<str:id>/", views.hire_candidate, name="hire_candidate"),
    path("schedule-interview/<str:application_id>/", views.schedule_interview,
         name="schedule_interview"),
]
