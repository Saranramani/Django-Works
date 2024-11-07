from django.db import models

class TodoClass(models.Model):
    todo = models.CharField(max_length=100)
    createdOn = models.DateTimeField(auto_now=True)
