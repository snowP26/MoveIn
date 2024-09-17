from django.db import models
# from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Tenant(models.Model):
    # First name, Last name, Email, Password, phone number
    # Tenant_email = models.EmailField(max_length=64, unique=True)
    # Tenant_password = models.CharField(max_length=64)
    # Tenant_phone = PhoneNumberField(unique=True,)
    Tenant_firstName = models.CharField(max_length=32)
    Tenant_lastName = models.CharField(max_length=32)

    def __str__(self):
        return()
    
class Property(models.Model):
    Property_name = models.TextField()
    Property_roomNum = models.IntegerField()

    def __str__(self):
        return(f"ID: {self.id} Name: {self.Property_name} Room Number: {self.Property_roomNum}")



class Room(models.Model):
    # is occupied
    Room_isOccupied = models.BooleanField(default=False)
    Room_image = models.ImageField(upload_to='assets', default='assets/test1.png')
    Room_tenant = models.CharField(max_length=128, default='Tenant')

    def __str__(self):
        return (f"ID:{self.id}: {self.Room_isOccupied} {self.Room_tenant}")


class Reports(models.Model):
    # report body tesxt
    # Reports_date =
    Reports_header = models.TextField()
    Reports_body = models.TextField()
    Reports_author = models.CharField(max_length=128)
    Reports_isCompleted = models.BooleanField(default=False)

    def __str__ (self):
        return (f"ID: {self.id} Header: {self.Reports_header}")

class Announcements(models.Model):
    # Announcement date
    Announce_header = models.TextField()
    Announce_body = models.TextField()

    def __str__(self): 
        return(f"ID: {self.id} Header: {self.Announce_header} Body: {self.Announce_body}")

