from django.db import models

from setup.models.department import Department

class Item(models.Model):
    name = models.CharField(max_length=18)
    description = models.TextField()
    department_id = models.ForeignKey(Department, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.name