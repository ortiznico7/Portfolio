from django.db import models

class Member(models.Model):
    firstname = models.CharField(max_length = 30)
    lastname = models.CharField(max_length = 30)
    member_id = models.CharField(max_length=20, unique=True)

class Account(models.Model):
    accounttype = models.CharField(max_length=200)
    amountinacc = models.CharField(max_length=200)
    ROI = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.accounttype} - {self.amountinacc}"
# Create your models here.

