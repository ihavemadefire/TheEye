from django.db import models
from django.core.validators import MaxValueValidator
from datetime import date
"""Models Module"""

# Create your models here.

class Event(models.Model):
    """Class for storing events"""
    session_id = models.CharField(max_length=36)
    category = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    data = models.JSONField()
    timestamp = models.DateTimeField(validators=[MaxValueValidator(limit_value=date.today)])
    
    def __str__(self):
        return self.session_id + '/' + self.category + '/' + self.name
