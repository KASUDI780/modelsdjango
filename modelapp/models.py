from django.db import models

# Create your models here.
class Students(models.Model):
    firstname=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.EmailField()
    gender=models.CharField(max_length=20,null=True)
    date_of_birth=models.DateField(null=True)

    def __str__(self):
        return self.firstname
# create a model class called contact;name,course,timing,mobile no, and gender
class Contact(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    course=models.CharField(max_length=50)
    time=models.DateTimeField()
    mobile_number=models.CharField(max_length=50)
    gender=models.CharField(max_length=50)
    age=models.CharField(max_length=50)

    def __str__(self):
        return self.first_name
