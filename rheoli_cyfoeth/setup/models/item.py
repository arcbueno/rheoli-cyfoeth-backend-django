from __future__ import annotations

from django.db import models
from django.forms import CharField

from setup.models.department import Department
from setup.models.moving_history import MovingHistory

class Item(models.Model):
    name: models.CharField = models.CharField(max_length=18)
    description: models.TextField = models.TextField(null=True)
    department: models.ForeignKey[Department] = models.ForeignKey(Department, on_delete=models.CASCADE)
    moving_history: models.ManyToManyField[MovingHistory, MovingHistory] = models.ManyToManyField(MovingHistory, null=True, blank=True)

    def __str__(self) -> str:
        return self.name