from django.test import TestCase
from api.models import Skill


class SkillModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Skill.objects.create(name='Python')

    def test_name_label(self):
        skill = Skill.objects.get(id=1)
        field_label = skill._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_name_max_length(self):
        skill = Skill.objects.get(id=1)
        max_length = skill._meta.get_field('name').max_length
        self.assertEqual(max_length, 255)

    def test_skill_str(self):
        skill = Skill.objects.get(id=1)
        expected_str = skill.name
        self.assertEqual(str(skill), expected_str)
