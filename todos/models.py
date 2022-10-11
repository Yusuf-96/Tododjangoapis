from django.db import models

# Create your models here.


class Todo(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title