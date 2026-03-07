from django.db import models

# Create your models here.
class StudySession(models.Model):
    date = models.DateField()
    topic = models.CharField(max_length=200)
    duration = models.IntegerField(help_text ="Duration in minutes")
    notes = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.topic} - {self.date}"