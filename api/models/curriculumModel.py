from django.db import models
from api.models.domainModel import Domain

from api.models.projectModel import Project
from api.models.skillsModel import Skill


class Curriculum(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    domain = models.ForeignKey(
        Domain, related_name="domain_set", on_delete=models.CASCADE
    )
    duration_in_months = models.PositiveIntegerField()
    skills_covered = models.ManyToManyField(Skill)
    projects = models.ManyToManyField(Project)

    def __str__(self):
        return self.name
