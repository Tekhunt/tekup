from django.db import models
from django.utils import timezone
from api.models.customUserModel import User
from api.models.mentorModel import Mentor

class Session(models.Model):
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE, related_name='mentor_sessions')
    mentee = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mentee_sessions')
    location = models.CharField(max_length=255)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    created_at = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)

    def __str__(self):
        return f'Session between {self.mentor} and {self.mentee}'

    class Meta:
        ordering = ['-created_at']
