from django.db import models
from django.utils import timezone

class Task(models.Model):
    task=models.CharField(max_length=255)
    creation_datetime=models.DateTimeField(default=timezone.now)
    due_datetime=models.DateTimeField()
    is_completed=models.BooleanField(default=False)

    def __str__(self):
        return f"{self.task}"
