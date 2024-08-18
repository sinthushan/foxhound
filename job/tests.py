from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Job, Stage

class JobTests(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.user = get_user_model().objects.create_user(
            username="testuser",
            email="test@test.com",
            password="pass",
        )
        cls.job = Job.objects.create(
            title = "Senior Analyst",
            company = "TD Bank",
            applicant = cls.user
        )
        cls.stage = Stage.objects.create(
            comment = "Just applied",
            job = cls.job,
            round = 0
        )
    def test_job_model(self):
        self.assertEqual(self.job.title, "Senior Analyst" )
        self.assertEqual(self.job.company, "TD Bank" )
        self.assertEqual(self.job.applicant.username, "testuser" )
        self.assertEqual(str(self.job), "Senior Analyst at TD Bank" )
    def test_stage_models(self):
        self.assertEqual(self.stage.stage, "AP")
        self.assertEqual(self.stage.job.title, "Senior Analyst")
        self.assertEqual(self.stage.comment, "Just applied")
        self.assertEqual(self.stage.round, 0)