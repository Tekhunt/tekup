from django.db import models
from django.utils.translation import gettext_lazy as _

from api.models.customUserModel import User
from api.models.skillsModel import Skill
from api.models.domainModel import Domain


class Mentee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="mentee")
    years_of_experience = models.IntegerField(
        _("years of experience"), blank=True, null=True
    )
    current_employer = models.CharField(
        _("current employer"), max_length=255, blank=True, null=True
    )
    bio = models.TextField(_("bio"), blank=True, null=True)
    skills = models.ManyToManyField(Skill, related_name="mentees")
    domain = models.ManyToManyField(Domain, related_name="mentees")

    def __str__(self):
        return (
            f"{self.user.first_name} {self.user.first_name}: {self.domain.name} Mentee"
        )
