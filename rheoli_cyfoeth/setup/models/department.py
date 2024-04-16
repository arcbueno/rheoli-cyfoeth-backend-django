from django.db import models
class Department(models.Model):
    name = models.CharField(max_length=18)
    description = models.TextField(null=True)
    
    def __str__(self) -> str:
        return self.name