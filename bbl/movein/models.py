from django.db import models
# from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Tenant(models.Model):
    # First name, Last name, Email, Password, phone number
    Tenant_firstName = models.CharField(max_length=32)
    Tenant_lastName = models.CharField(max_length=32)
    Tenant_email = models.EmailField(max_length=64, unique=True)
    Tenant_password = models.CharField(max_length=64)
    # Tenant_phone = PhoneNumberField(unique=True,)

class Room(models.Model):
    # is occupied
    Room_isOccupied = models.BooleanField(default=False)
    Room_image = models.ImageField(upload_to='assets', default='assets/test1.png')

class Reports(models.Model):
    # report body tesxt
    Reports_body = models.TextField()
    Reports_author = models.CharField(max_length=128)
    # Reports_date =
    Reports_isCompleted = models.BooleanField(default=False)
     
# omsim