from django.db import models

# Create your models here.
class Data(models.Model):
    name=models.CharField(max_length=50)
    description=models.CharField(max_length=500,default=" ")
    image=models.ImageField(upload_to="images/",default=" ")

    def __str__(self):
        return self.name
    
class Founder(models.Model):
    fname=models.CharField(max_length=50)
    fdescription=models.CharField(max_length=500,default=" ")
    fimage=models.ImageField(upload_to="images1/",default=" ")

    def __str__(self):
        return self.fname
    
class Contact(models.Model):
    email=models.EmailField()
    name=models.CharField(max_length=50)
    mnumber=models.CharField(max_length=10)
    msg=models.CharField(max_length=100)
    
    
    def __str__(self):
        return self.name
    
class Job(models.Model):
    role=models.CharField(max_length=50)
    salary=models.CharField(max_length=50)
    experiance=models.CharField(max_length=100)
    Rskill=models.CharField(max_length=100)
    location=models.CharField(max_length=100,default='')
    
    def __str__(self):
        return self.role
    
class Apply(models.Model):
    email=models.EmailField()
    name=models.CharField(max_length=50)
    mnumber=models.CharField(max_length=10)
    # resume=models.FileField(upload_to="resumes/",default=" ")
    
    
    def __str__(self):
        return self.name
    