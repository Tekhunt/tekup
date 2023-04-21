from django.db import models
from django.utils.translation import gettext_lazy as _

from api.models.customUserModel import User
from api.models.domainModel import Domain
from api.models.menteeModel import Skill


class Mentor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="mentor")
    years_of_experience = models.IntegerField(_("years of experience"), blank=True, null=True)
    current_employer = models.CharField(_("current employer"), max_length=255, blank=True, null=True)
    bio = models.TextField(_("bio"), blank=True, null=True)
    skills = models.ManyToManyField(Skill, related_name="mentors")
    domain = models.ManyToManyField(Domain, related_name="mentors")
    available = models.BooleanField(_("available"), default=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.first_name}: {self.domain.name} Mentor"