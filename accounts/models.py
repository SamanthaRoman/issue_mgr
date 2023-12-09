from django.db import models
#1 import abstract user model
from django.contrib.auth.models import AbstractUser

# 2 Create your models here. one for Role, Team and our regular custom user.

class Role(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=256)

    def __str__(self):      # dunder method 
        return self.name        #will show the name of the role in the drop down methond.


class Team(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class CustomUser(AbstractUser):
    role = models.ForeignKey(
        Role, 
        on_delete=models.CASCADE, 
        null=True, blank=True    #null=true means the database can be left emptied, blank true means the form field can be left empty also. 
        )      

    team = models.ForeignKey(
        Team, 
        on_delete=models.CASCADE,
        null=True, blank=True   
    )