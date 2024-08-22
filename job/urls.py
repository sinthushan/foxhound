from django.urls import path
from .views import JobList, JobDetail, StageCreate


urlpatterns = [
    path("<int:pk>/", JobDetail.as_view(), name="job_detail"),
    path("stages/", StageCreate.as_view(), name="stage_create"),
    path("", JobList.as_view(), name="job_list"),  
]