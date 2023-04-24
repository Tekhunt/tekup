from django.test import TestCase
from api.models import SkillCovered

class SkillCoveredModelTestCase(TestCase):

    def setUp(self):
        self.skill1 = SkillCovered.objects.create(name="Skill 1", description="Description of skill 1")
        self.skill2 = SkillCovered.objects.create(name="Skill 2", description="Description of skill 2")

    def test_skill_covered_model(self):
        self.assertEqual(self.skill1.name, "Skill 1")
        self.assertEqual(self.skill1.description, "Description of skill 1")
        self.assertEqual(self.skill2.name, "Skill 2")
        self.assertEqual(self.skill2.description, "Description of skill 2")
        self.assertEqual(str(self.skill1), "Skill 1")
        self.assertEqual(str(self.skill2), "Skill 2")

   