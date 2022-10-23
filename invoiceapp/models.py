import email
from operator import mod
from statistics import mode
from django.db import models

# Create your models here.

class AdminInfo(models.Model):
    email=models.TextField()
    password=models.TextField()
    date_created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

class Links(models.Model):
    link=models.TextField()
    email=models.TextField(null=True)
    date_created=models.DateField(auto_now_add=True)
    password=models.TextField(null=True)

    

class User(models.Model):
    email=models.TextField()
    password=models.TextField(null=True)
    date_created=models.DateField(auto_now_add=True)
    # links=models.ForeignKey(
    #     Links, null=True,blank=True,on_delete=models.CASCADE
    # )
    links = models.ManyToManyField(Links)

    def __str__(self):
        return self.email or ""


# class User(models.Model):
#     email=models.TextField()
#     date_created=models.DateField(auto_now_add=True)

# class Links(models.Model):
#     link=models.TextField()
#     date_created=models.DateField(auto_now_add=True)
#     userBelongs=models.ForeignKey(
#         User,null=True,blank=True,on_delete=models.CASCADE
#     )