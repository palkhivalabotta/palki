from django.db import models

# Create your models here.
class UserRegister(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email_id = models.EmailField(max_length=20, primary_key=True)
    password = models.CharField(max_length=50)
    rpassword = models.CharField(max_length=50)
    contact_no = models.IntegerField()
    address = models.CharField(max_length=100)

class Contact(models.Model):
    name=models.CharField(max_length=20)
    Email_id=models.EmailField(max_length=20,primary_key=True)
    phone_no=models.IntegerField()
    message=models.CharField(max_length=220)

class payment(models.Model):
    Fullname=models.CharField(max_length=20)
    Room_type=models.CharField(max_length=20)
    Check_in=models.DateField()
    Check_out=models.DateField()
    Contact_no=models.IntegerField()
    Address=models.CharField(max_length=50)
    Total_amount = models.DecimalField(max_digits=10, decimal_places=4)
    Card_no=models.IntegerField()
    Card_type=models.CharField(max_length=20)




'''class display(models.Model):
    Name=models.CharField(max_length=20)
    Contact_no = models.IntegerField()
    room_type=models.CharField(max_length=20)
    Check_in=models.DateField()
    Check_out=models.DateField()
    Address=models.CharField(max_length=20)
    Cust_Id=models.AutoField(primary_key=True)
    Total_amount=models.DecimalField(max_digits=10,decimal_places=4)'''




class Cancel(models.Model):
    Uname=models.CharField(max_length=20)
    Room_no=models.IntegerField()
    Cust_id=models.IntegerField()