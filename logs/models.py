from django.db import models
from django.contrib.auth.models import User

class StudySession(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  
    topic = models.CharField(max_length=200)
    week_number = models.IntegerField(default=0)
    date = models.DateField()
    duration_minutes = models.PositiveIntegerField(default=0)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.topic} (Week {self.week_number})"