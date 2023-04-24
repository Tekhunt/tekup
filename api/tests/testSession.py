from django.test import TestCase
from django.utils import timezone
from api.models.customUserModel import User
from api.models.mentorModel import Mentor
from api.models.sessionModel import Session


class SessionModelTestCase(TestCase):
    def setUp(self):
        self.mentor = Mentor.objects.create(
            user=User.objects.create(
                email="mentor@example.com",
                first_name="John",
                last_name="Doe",
                is_mentor=True,
                is_mentee=False,
            )
        )
        self.mentee = User.objects.create(
            email="mentee@example.com",
            first_name="Jane",
            last_name="Doe",
            is_mentor=False,
            is_mentee=True,
        )
        self.session = Session.objects.create(
            mentor=self.mentor,
            mentee=self.mentee,
            location="Online",
            start_time=timezone.now(),
            end_time=timezone.now() + timezone.timedelta(hours=1),
            description="Session description",
        )

    def test_str_representation(self):
        expected = f"Session between {self.mentor} and {self.mentee}"
        self.assertEqual(str(self.session), expected)

    def test_ordering(self):
        session1 = Session.objects.create(
            mentor=self.mentor,
            mentee=self.mentee,
            location="Online",
            start_time=timezone.now(),
            end_time=timezone.now() + timezone.timedelta(hours=1),
            description="Session description",
            created_at=timezone.now() - timezone.timedelta(days=1),
        )
        session2 = Session.objects.create(
            mentor=self.mentor,
            mentee=self.mentee,
            location="Online",
            start_time=timezone.now(),
            end_time=timezone.now() + timezone.timedelta(hours=1),
            description="Session description",
            created_at=timezone.now() - timezone.timedelta(days=2),
        )
        sessions = Session.objects.all()
        self.assertEqual(list(sessions), [self.session, session1, session2])
