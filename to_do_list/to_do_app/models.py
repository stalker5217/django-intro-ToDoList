from django.db import models

# Create your models here.
# models.py = DTO와 유사한 역할

# Create your models here.
class Todo(models.Model):
    content = models.CharField(max_length = 255)
    isDone = models.BooleanField(default=False)