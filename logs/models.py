from django.db import models

class StudySession(models.Model):  # If you named this StudySession, change it to Session
    topic = models.CharField(max_length=200)
    week_number = models.IntegerField(default=0)
    date = models.DateField()
    duration_minutes = models.PositiveIntegerField(default=0)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.topic} (Week {self.week_number})"