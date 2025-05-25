from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)
    description = models.TextField()

    def __str__(self):
        return self.name
