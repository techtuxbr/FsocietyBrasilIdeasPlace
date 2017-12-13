from django.db import models
from django.contrib.auth.models import User


class Project(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=220)
    slug = models.CharField(max_length=230)
    slogan = models.TextField(max_length=120)
    description = models.TextField()
    details = models.TextField()
    authorID = models.ForeignKey(User, on_delete=models.CASCADE)
    picture = models.CharField(max_length=240)
# Create your models here.
