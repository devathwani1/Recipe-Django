from django.db import models

# Create your models here.

class Student(models.Model):
    #id = models.AutoField()
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(null=True,blank = True)
    address = models.TextField(null=True,blank = True)
  

class Car(models.Model):
    car_name = models.CharField(max_length=100)
    speed = models.IntegerField()

    def __str__(self) -> str:
        return self.car_name