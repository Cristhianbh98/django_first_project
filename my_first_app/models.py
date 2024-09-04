from django.db import models

# Create your models here.
class Car(models.Model):
    name = models.TextField(max_length=250)
    year = models.TextField(max_length=4, null=True)
    color = models.TextField(max_length=50, null=True)

    def __str__(self):
        return f"{self.name} - {self.year}"

