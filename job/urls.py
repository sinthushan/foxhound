from django.urls import path
from .views import JobList, JobDetail, StageCreate


urlpatterns = [
    path("jobs/<int:pk>/", JobDetail.as_view(), name="job_detail"),
    path("jobs/", JobList.as_view(), name="job_list"),
    path("stages/", StageCreate.as_view(), name="stage_create")
]