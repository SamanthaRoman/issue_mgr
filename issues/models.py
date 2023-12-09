from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse


# Create your models here.


class Status(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=256)

    def __str__(self):
        return self.name # we need this so the drop down uses the status names.

class Issue(models.Model):
    summary = models.CharField(max_length=128)
    description = models.TextField()  #text field also allows images.
    reporter = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE    #Cascade is a constraigte on foregin keys. Insures that all the issues are also deleted when the user
    )
    assignee = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name="assignee",   #sets this as a label so theres no confusion between the two foregn keys going to the same models 
    )
    status = models.ForeignKey(
        Status,
        on_delete=models.CASCADE,
    )
    created_on = models.DateTimeField(auto_now_add=True)
    is_archived = models.BooleanField(default=False)    #set default to False so it doesn't start as archived

    def __str__(self):
        return self.summary[:128]       #you can python slize to specify what character to what character to make it show up as less. The zero is complicit so you only need to specify up to 128 or what ever number you want.
    
    def get_absolute_url(self):
        return reverse("detail", args=[self.id])      #looks for url patters to define what you want to see more detail on. Reverse allows us to look up based on the name attribute so for in this case is detail. 
