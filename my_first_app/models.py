from django.db import models

# Create your models here.
class Car(models.Model):
    name = models.TextField(max_length=250)
    year = models.TextField(max_length=4, null=True)
    color = models.TextField(max_length=50, null=True)

    def __str__(self):
        return f"{self.name} - {self.year}"

class Publisher(models.Model):
    name = models.TextField(max_length=250, null=True)
    address = models.TextField(max_length=250, null=True)
    city = models.TextField(max_length=100, null=True)
    state_province = models.TextField(max_length=100, null=True)
    country = models.TextField(max_length=100)
    website = models.URLField()

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.TextField(max_length=250)
    birth_date = models.DateField()

    def __str__(self):
        return self.name

class Profile(models.Model):
    author = models.OneToOneField(Author, on_delete=models.CASCADE)
    website = models.URLField()
    biography = models.TextField(max_length=250)

class Book(models.Model):
    title = models.TextField(max_length=250)
    publication_date = models.DateField()
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    authors = models.ManyToManyField(Author, related_name='authors')

    def __str__(self):
        return self.title
