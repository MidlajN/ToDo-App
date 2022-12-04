from django.db import models


# Create your models here.
class Task(models.Model):
    task1 = models.TextField()
    priority = models.IntegerField(default='0')

    def __str__(self):
        return self.task1

