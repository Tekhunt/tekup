from django.test import TestCase
from django.conf import settings
from django.utils import timezone
from api.models.notificationModel import Notification
from api.models.customUserModel import User


class NotificationModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            email="test@example.com",
            first_name="John",
            last_name="Doe",
            is_mentor=False,
            is_mentee=True,
        )
        self.notification = Notification.objects.create(
            user=self.user,
            message="Test notification",
            timestamp=timezone.now(),
            read=False,
        )

    def test_str_representation(self):
        expected = "Test notification"
        self.assertEqual(str(self.notification), expected)