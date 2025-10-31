from django.db import models

class TodoItem(models.Model):
    title = models.CharField(max_length=200, blank=False)  
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title