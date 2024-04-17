from django.db import models
class Department(models.Model):
    name = models.CharField(max_length=18)
    description = models.TextField(null=True)
    # TODO: Add Employee key
    
    def __str__(self) -> str:
        return self.name