from django.db import models

from setup.models.department import Department

class MovingHistory(models.Model):
    start_date = models.DateTimeField(null=True)
    finish_date = models.DateTimeField(unique=True)
    initial_department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='initial_department')
    destination_department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='destination_department')
    item_id = models.PositiveIntegerField()
    