from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    email=models.EmailField(unique=True)


#creating for account mode
class Users(models.Model): #aquiring the properties meaning
    username=models.CharField(max_length=100,unique=True)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=100)


#creating for account mode
class Movie(models.Model): #aquiring the properties meaning
    movie_name=models.CharField(max_length=100,unique=True)
    date=models.CharField(max_length=100)
    rating=models.IntegerField()

#creating for account mode
class Movie_review(models.Model): #aquiring the properties meaning
    movie_name=models.CharField(max_length=100,unique=True)
    date=models.CharField(max_length=100)
    rating=models.IntegerField()
    budget=models.CharField(max_length=100)