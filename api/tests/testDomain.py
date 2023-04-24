from django.test import TestCase
from api.models.domainModel import Domain


class DomainTestCase(TestCase):
    def setUp(self):
        Domain.objects.create(name="Technology")
        Domain.objects.create(name="Marketing")

    def test_domain_names(self):
        """Domain names are correctly stored and retrieved"""
        tech = Domain.objects.get(name="Technology")
        marketing = Domain.objects.get(name="Marketing")
        self.assertEqual(tech.name, "Technology")
        self.assertEqual(marketing.name, "Marketing")

    def test_domain_str_method(self):
        """Domain's __str__ method returns the domain name"""
        tech = Domain.objects.get(name="Technology")
        marketing = Domain.objects.get(name="Marketing")
        self.assertEqual(str(tech), "Technology")
        self.assertEqual(str(marketing), "Marketing")
