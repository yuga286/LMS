from django.db import models
# from .author import Author 
# from python_pro_LMS.urls import *

class Info(models.Model):
    First_Name = models.CharField(max_length=100)
    Middle_Name = models.CharField(max_length=100)
    Last_Name = models.CharField(max_length=100)
    User_Name = models.CharField(max_length=100)
    Contact_Number = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    
    class Meta:
        db_table = 'Student_Data'

class Author(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Book(models.Model):
    Book_ID = models.AutoField(primary_key=True)
    Book_Name = models.CharField(max_length=256, blank=False)
    author = models.ForeignKey('Author', on_delete=models.CASCADE, null=True, blank=True)
    Book_Count=models.IntegerField()
    Publication_Year = models.DateTimeField(blank=True, null=True)
    Publisher = models.CharField(max_length=100, blank=True)
    
    class Meta:
        db_table='Book_Data'

    def __str__(self):
        return self.Book_Name