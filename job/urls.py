from django.urls import path
from .views import JobList, JobDetail


urlpatterns = [
    path("<int:pk>/", JobDetail.as_view(), name="job_detail"),
    path("", JobList.as_view(), name="job_list")
]