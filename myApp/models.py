from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.PositiveIntegerField(null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    

class PoliceOfficer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='police_officer', null=True, blank=True)
    badge_number = models.CharField(max_length=20)
    name = models.CharField(max_length=100,default='')
    email = models.EmailField(default='user@gmail.com',unique=True)
    gender = models.CharField(max_length=1, choices=[('M', 'Male'), ('F', 'Female')]) 
    age = models.PositiveIntegerField()
    contact = models.CharField(max_length=100)
    rank = models.CharField(max_length=50)
    department = models.CharField(max_length=100)
    
class Complaint(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=1, choices=[('M', 'Male'), ('F', 'Female')])
    phone = models.CharField(max_length=10)
    place = models.CharField(max_length=100)
    description = models.TextField()
    is_solved = models.BooleanField(default=False)
    CATEGORY_CHOICES = [
        ('robbery', 'Robbery'),
        ('assault', 'Assault'),
        ('fraud', 'Fraud'),
        ('murder', 'Murder'),
        ('burglary', 'Burglary'),
        ('abuse', 'Abuse'),
        ('kidnapping', 'Kidnapping'),
        ('cybercrime', 'Cyber Crime'),
        ('other', 'Other'),
    ]

    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='other')

class MissingPerson(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    missing_person_name = models.CharField(max_length=255, blank=True, null=True)
    missing_person_description = models.TextField(blank=True, null=True)
    missing_person_photo = models.ImageField(upload_to='missing_person_photo/', blank=True, null=True)
    age = models.IntegerField(default=1)
    gender = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')],blank=True, null=True)
    contact_number = models.CharField(max_length=10, blank=True, null=True)
    
    def __str__(self):
        return self.missing_person_name

