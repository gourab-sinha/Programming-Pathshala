from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100, null=False)
    email = models.CharField(max_length=300, null=False)
    picture = models.CharField(max_length=300, null=True)
