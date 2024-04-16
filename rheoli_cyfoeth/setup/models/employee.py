from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=50)
    is_admin = models.BooleanField(default=False)
    
    
    def __str__(self) -> str:
        return self.name