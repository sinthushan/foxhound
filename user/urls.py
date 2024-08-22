from django.urls import path
from .views import ApplicantDetail


urlpatterns = [
    path("<int:pk>/", ApplicantDetail.as_view(), name="job_detail"),
]