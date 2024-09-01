from django.urls import path
from .views import ApplicantDetail


urlpatterns = [
    path("", ApplicantDetail.as_view(), name="applicant_detail"),
]