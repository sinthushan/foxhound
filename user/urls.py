from django.urls import path
from .views import ApplicantDetail, link_account


urlpatterns = [
    path("", ApplicantDetail.as_view(), name="applicant_detail"),
    path("link/", link_account,name='link_account')
]