from django.db import models

class Author(models.Model):
	first_name=models.CharField(max_length=30)
	last_name=models.CharField(max_length=40)
	email=models.EmailField()

class Book(models.Model):
	title=models.CharField(max_length=100)
	authors=models.ManyToManyField(Author)
	publication_date=models.DateField()

# Create your models here.
