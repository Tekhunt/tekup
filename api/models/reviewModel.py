from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from api.models.menteeModel import Mentee
from api.models.mentorModel import Mentor


class Review(models.Model):
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE)
    mentee = models.ForeignKey(Mentee, on_delete=models.CASCADE)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    comment = models.TextField(max_length=500, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
    
    def __str__(self):
        return f"Review between {self.mentor.first_name} {self.mentee.last_name}"
