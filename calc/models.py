from django.db import models

# Create your models here.
class data(models.Model):
    code = models.CharField(max_length=100) 
    type=models.CharField(max_length=100)      
    name = models.CharField(max_length=100)               
    branch1 = models.CharField(max_length=100) 
    semester1 = models.CharField(max_length=100) 
    branch2 = models.CharField(max_length=100) 
    semester2 = models.CharField(max_length=100) 
    branch3 = models.CharField(max_length=100) 
    semester3 = models.CharField(max_length=100) 
    classroom_code1 = models.CharField(max_length=100)
    classroom_code2 = models.CharField(max_length=100) 
    classroom_code3 = models.CharField(max_length=100)
    faculty1 = models.CharField(max_length=100)
    faculty2 = models.CharField(max_length=100)
    faculty3 = models.CharField(max_length=100)           
    theory = models.IntegerField()
    tutorial = models.IntegerField()
    lab = models.IntegerField()
    lab_name = models.CharField(max_length=100) 

