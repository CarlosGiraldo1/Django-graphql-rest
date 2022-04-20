from djongo import models
from django.utils import timezone

class Company(models.Model):
    _id = models.ObjectIdField()
    name = models.CharField(max_length=50)
    state = models.PositiveIntegerField(default=0)
    creationDate = models.DateTimeField(default=timezone.now, editable=False)