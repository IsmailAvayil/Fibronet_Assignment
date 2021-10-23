from django.db import models
from datetime import datetime


# Create your models here.
class Login (models.Model):
    User_Name = models.CharField(max_length=20)
    Password = models.CharField(max_length=10)
    Account=models.CharField(max_length=10)
    status=models.IntegerField()
class Customer_Reg(models.Model):
    Customer_type=models.CharField(max_length=10)
    Pre_Postpaid_type = models.CharField(max_length=10)
    Applied_plan = models.CharField(max_length=10)
    Register_ID = models.CharField(max_length=10)
    Registration_date = models.DateField(max_length=10)
    Date_of_Birth = models.CharField(max_length=10)
    Full_Name = models.CharField(max_length=10)
    Address = models.CharField(max_length=50)
    Email= models.EmailField(max_length=10)
    Mobile_no = models.CharField(max_length=10)
    H_no = models.IntegerField()
    Mobile_no = models.CharField(max_length=10)
    Village_Colony= models.CharField(max_length=10)
    City = models.CharField(max_length=10)
    State = models.CharField(max_length=10)
    District = models.CharField(max_length=10)
    Main_Locality = models.CharField(max_length=10)
    User_Name=models.CharField(max_length=10)

class Worker_Reg(models.Model):
    Lineworker_ID=models.CharField(max_length=10)
    Full_Name=models.CharField(max_length=15)
    Age=models.CharField(max_length=5)
    Address=models.CharField(max_length=50)
    Email=models.CharField(max_length=15)
    Mobile_no=models.CharField(max_length=15)
    User_Name = models.CharField(max_length=10)

class Plans_Reg(models.Model):
    Plan1=models.CharField(max_length=20)
    Plan1_Det = models.CharField(max_length=20)
    Plan2 = models.CharField(max_length=20)
    Plan2_Det = models.CharField(max_length=20)
    Plan3 = models.CharField(max_length=20)
    Plan3_Det = models.CharField(max_length=20)
    Plan4 = models.CharField(max_length=20)
    Plan4_Det = models.CharField(max_length=20)
    Plan5=models.CharField(max_length=20)
    Plan5_Det = models.CharField(max_length=20)
    Plan6=models.CharField(max_length=20)
    Plan6_Det = models.CharField(max_length=20)
    Plan7=models.CharField(max_length=20)
    Plan7_Det = models.CharField(max_length=20)
class Admin_Request(models.Model):
    Customer_type=models.CharField(max_length=10)
    Applied_plan = models.CharField(max_length=10)
    Full_Name = models.CharField(max_length=10)
    Address = models.CharField(max_length=50)
    Mobile_no = models.CharField(max_length=10)
    H_no = models.IntegerField()
    Village_Colony= models.CharField(max_length=10)
    City = models.CharField(max_length=10)
    Main_Locality = models.CharField(max_length=10)
    Customer_Complaint=models.CharField(max_length=500)

class Customer_complaints(models.Model):
    Register_ID=models.CharField(max_length=10)
    Full_Name=models.CharField(max_length=12)
    Subject=models.CharField(max_length=20)
    Message=models.CharField(max_length=500)









