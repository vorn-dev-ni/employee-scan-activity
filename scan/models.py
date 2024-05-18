from django.db import models
from enum import Enum
import datetime
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CompanyOutlet (models.Model) :
 address = models.CharField(max_length=255,null=False, blank=False)
 provinces = models.CharField(max_length=255,null=False, blank=False)
 lati = models.DecimalField(blank=False,null=False,max_digits=20,decimal_places=6)
 lon = models.DecimalField(max_length=255,null=False,max_digits=20,decimal_places=6 )
 

# class CheckinType (models.Model):
#    check_type = models.CharField(max_length=50,default="in")

#    def __str__(self):
#        return self.check_type
   

class CheckinTypeEnum(Enum):
    IN = 'IN'
    OUT = 'OUT'
    
    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]
    
    
class ROLES (models.Model) :
    type = models.CharField(max_length=40,null=False)

    def __str__(self):
        return self.type
    
class Employee(models.Model):
    STATE_TYPE = [
        ("pending", "Pending"),
        ("approved", "Approved"),
         ("rejected", "Rejected")
    ]
    
    username = models.CharField(max_length=200,null=False,blank=False,default=datetime.datetime.now())
    email = models.EmailField(max_length=255,unique=True,null=False)
    status = models.CharField(max_length=25,default="pending",choices=STATE_TYPE)
    password = models.CharField(max_length=200,null=False,blank=False,default="12345")
    role = models.ForeignKey(
     
        ROLES,
           on_delete=models.CASCADE,
           null=True,
        
      
        related_name="employees",
     
    
        
    )
    company = models.ForeignKey(
     
        CompanyOutlet,
           on_delete=models.CASCADE,
           null=True,
        
      
        related_name="employees",
    
        
    ) 
    def __str__(self):
        return self.email +"-" + self.status
    
class ActivityEmployee (models.Model) :
 CHECKIN_TYPE_CHOICES = [
        ("IN", "Check In"),
        ("OUT", "Check Out")
    ]
 emp_id = models.ForeignKey(
Employee,
related_name="activities",
on_delete=models.CASCADE
 )
 
 date = models.DateField(null=True,blank=True,auto_now_add=True)
 times = models.TimeField(blank=False,null=False)
 types = models.CharField(
        max_length=5,
        choices=CHECKIN_TYPE_CHOICES,
        default="IN"
    )
 lati = models.DecimalField(blank=True,null=True,max_digits=20,decimal_places=6)
 lon = models.DecimalField(max_length=255,blank=True,null=True,max_digits=20,decimal_places=6 ) 
#  checkin_type = models.ForeignKey(
#     CheckinType,
#     on_delete=models.DO_NOTHING,related_name="act_log"
#  )

 def __str__(self):
        return str(self.date) 

class AccessToken(models.Model):
    emp_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    token = models.CharField(max_length=500)
    refresh = models.CharField(max_length=500,null=True,blank=True) 
    created_at = models.DateTimeField(auto_now_add=True)
