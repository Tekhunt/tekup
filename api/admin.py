from django.contrib import admin
from api.models.curriculumModel import Curriculum

from api.models.customUserModel import User
from api.models.domainModel import Domain
from api.models.menteeModel import Mentee
from api.models.mentorModel import Mentor
from api.models.projectModel import Project
from api.models.reviewModel import Review
from api.models.skillCoveredModel import SkillCovered
from api.models.skillsModel import Skill

# Register your models here.
admin.site.register(User)
admin.site.register(Mentor)
admin.site.register(Mentee)
admin.site.register(Skill)
admin.site.register(Domain)
admin.site.register(Review)
admin.site.register(SkillCovered)
admin.site.register(Project)
admin.site.register(Curriculum)






