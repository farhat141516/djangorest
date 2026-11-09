from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    cours = models.CharField(max_length=20, default='Python')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
