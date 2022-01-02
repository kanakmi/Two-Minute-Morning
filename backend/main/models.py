from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


class todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    dec = models.TextField()
    date = models.DateField(default=now)
    completed= models.BooleanField(default=False)

class sins(models.Model):
    user = models.ForeignKey(User,models.CASCADE)
    desc = models.TextField()
    date = models.DateField(default=now)


class goods(models.Model):
    user = models.ForeignKey(User,models.CASCADE)
    desc = models.TextField()
    date = models.DateField(default=now)