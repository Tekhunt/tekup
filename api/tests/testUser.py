from django.test import TestCase
from api.models import User

class UserModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(email='test@example.com', first_name="user1", last_name="user1",is_mentor=True, is_mentee=False)

    def test_user_string_representation(self):
        self.user.save()
        self.assertEqual(str(self.user), 'user1 user1')
        
    def test_user_is_mentor(self):
        self.assertTrue(self.user.is_mentor)
        self.assertFalse(self.user.is_mentee)
        
    def test_user_is_active(self):
        self.assertTrue(self.user.is_active)
        
    def test_user_is_staff(self):
        self.assertFalse(self.user.is_staff)
