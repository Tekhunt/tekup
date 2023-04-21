from django.contrib import admin

from api.models.customUserModel import User
from api.models.domainModel import Domain
from api.models.menteeModel import Mentee
from api.models.mentorModel import Mentor
from api.models.reviewModel import Review
from api.models.skillsModel import Skill

# Register your models here.
admin.site.register(User)
admin.site.register(Mentor)
admin.site.register(Mentee)
admin.site.register(Skill)
admin.site.register(Domain)
admin.site.register(Review)



