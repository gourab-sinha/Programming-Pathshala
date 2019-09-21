from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Course(models.Model):
    course_name = models.CharField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.course_name