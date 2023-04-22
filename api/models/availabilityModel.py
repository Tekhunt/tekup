from django.db import models


class Availability(models.Model):
    day_of_week = models.IntegerField(
        choices=[(i, i) for i in range(7)]
    )  # 0 = Monday, 1 = Tuesday, etc.
    start_time = models.TimeField()
    end_time = models.TimeField()
