from django.test import TestCase
from api.models import Project

class ProjectModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Project.objects.create(name='Project A', description='This is Project A')
        Project.objects.create(name='Project B', description='This is Project B')
    
    def test_name_label(self):
        project = Project.objects.get(id=1)
        field_label = project._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')
    
    def test_description_label(self):
        project = Project.objects.get(id=1)
        field_label = project._meta.get_field('description').verbose_name
        self.assertEquals(field_label, 'description')
    
    def test_name_max_length(self):
        project = Project.objects.get(id=1)
        max_length = project._meta.get_field('name').max_length
        self.assertEquals(max_length, 255)
    
    def test_object_name_is_name(self):
        project = Project.objects.get(id=1)
        expected_object_name = f'{project.name}'
        self.assertEquals(expected_object_name, str(project))
    
    def test_project_count(self):
        self.assertEquals(Project.objects.count(), 2)
