# import datetime
# from django.test import TestCase
# from api.models.customUserModel import User
# from api.models.domainModel import Domain
# from api.models.menteeModel import Skill
# from api.models.availabilityModel import Availability
# from api.models.mentorModel import Mentor
# # from api.models.mentorModel import Mentor


# class MentorModelTestCase(TestCase):
#     def setUp(self):
#         self.user = User.objects.create(
#             email="test@example.com",
#             first_name="John",
#             last_name="Doe",
#             is_mentor=True,
#             is_mentee=False,
#         )
#         # self.mentor.skills = ['skill1', 'skill2']
#         self.domain = Domain.objects.create(name="Test Domain")
#         self.skill = Skill.objects.create(name="Test Skill")
#         self.availability = Availability.objects.create(day_of_week=0, start_time='09:00:00', end_time='12:00:00')
#         self.mentor = Mentor.objects.create(
#             user=self.user,
#             years_of_experience=5,
#             current_employer="Test Company",
#             bio="Test Bio",
#             domain=self.domain,
#             availability=self.availability
#         )
#         self.mentor.domain.add(self.domain)
#         self.mentor.skills.add(self.skill)
#         self.mentor.available.add(self.availability)

#     def test_mentor_model(self):
#         self.assertTrue(isinstance(self.mentor, Mentor))
#         self.assertEqual(self.mentor.user.first_name, "John")
#         self.assertEqual(self.mentor.user.last_name, "Doe")
#         self.assertEqual(self.mentor.years_of_experience, 5)
#         self.assertEqual(self.mentor.current_employer, "Test Company")
#         self.assertEqual(self.mentor.bio, "Test Bio")
#         self.assertEqual(self.mentor.skills.first().name, "Test Skill")
#         self.assertEqual(self.mentor.domain.first().name, "Test Domain")
#         self.assertEqual(self.mentor.available.first().day_of_week, 0)
#         self.assertEqual(self.mentor.available.first().start_time, datetime.time(9, 0))
#         self.assertEqual(
#             str(self.mentor), "John Doe: Test Domain Mentor"
#         )

