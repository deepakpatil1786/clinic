
import email
import profile
from random import choices
from telnetlib import STATUS 
from django.db import models
from datetime import date

# Create your models here.
class User(models.Model):

    GENDER_MALE = 0
    GENDER_FEMALE = 1
    GENDER_CHOICES = [(GENDER_MALE, 'Male'), (GENDER_FEMALE, 'Female')]
    
    role=(
        ('admin','Admin'),
        ('doctor','Doctor'),
        ('patient','Patient'),
    )

    role=models.CharField(max_length=50,choices=role)
    name=models.CharField(max_length=50)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=20)
    clinic=models.CharField(max_length=50,default=None,blank=True,null=True)
    gender=models.IntegerField(choices=GENDER_CHOICES,default=None,blank=True,null=True)
    speciality=models.CharField(max_length=50,default=None,blank=True,null=True)
    Address=models.CharField(max_length=30,default=None,blank=True,null=True)
    profile=models.FileField(upload_to='profile',default='profile.png')

    def __str__(self):
        return self.name 


class SLOT(models.Model):

    TIME_SLOT = (
        (1, '10:00 am -11:00 am'),
        (2, '11:00 am - 12:00 pm'),
        (3, '12:00 pm- 1:00 pm'),
        (4, '1:00 pm - 2:00 pm'),
        (5, '2:00 pm- 3:00 pm'),
        (6, '3:00 pm - 4:00 pm'),
        (7, '4:00 pm - 5:00 pm'),
    )

    WEEK_SLOT =(
        (1,'mon'),
        (2,'tue'),
        (3,'wed'),
        (4,'thu'),
        (5,'fri'),
        (6,'sat'),
        (7,'sun'),
    )

    doctor = models.ForeignKey(User,on_delete = models.CASCADE)
    timeslot = models.IntegerField(choices = TIME_SLOT)
    weekslot = models.IntegerField(choices = WEEK_SLOT)


    def __int__ (self):
        return self.timeslot +'@'+ self.weekslot



class Appointment(models.Model):

    STATUS = (
         (0,'Pending'),
         (1,'Completed'),
         (2,'Absent'),
         (3,'Cancel'),
    )

    slot = models.ForeignKey(SLOT,on_delete=models.CASCADE)
    patient_id = models.IntegerField()
    patient_name = models.CharField(max_length=50)
    weekslot = models.IntegerField()
    timeslot = models.IntegerField()
    decription = models.TextField(max_length=50)
    status = models.IntegerField(default=0,choices=STATUS)
    date =models.DateField()

    def __int__(self):
        return self.patient_id

    def __str__(self):
        return self.patient_name
    



     
