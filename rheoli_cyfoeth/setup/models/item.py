from django.db import models

from setup.models.department import Department
from setup.models.moving_history import MovingHistory

class Item(models.Model):
    name = models.CharField(max_length=18)
    description = models.TextField(null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    moving_history = models.ManyToManyField(MovingHistory, null=True, blank=True)
    
    def __str__(self) -> str:
        return self.name