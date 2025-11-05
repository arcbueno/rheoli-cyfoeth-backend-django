from __future__ import annotations

from django.db import models
from django.contrib.auth.models import User

class Department(models.Model):
    name: models.CharField = models.CharField(max_length=18)
    description: models.TextField = models.TextField(null=True)
    manager: models.ForeignKey[User] = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    
    def __str__(self) -> str:
        return self.name
