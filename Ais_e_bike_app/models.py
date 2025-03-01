from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager , AbstractBaseUser , PermissionsMixin



class customUserManager(BaseUserManager):
    def create_user(self,email,username=None,password=None,**extra_fields):
        if not email:
            raise ValueError('You did not entered a valid email')
        
        email = self.normalize_email(email)
        user = self.model(email=email,username=username, **extra_fields)
        user.set_password(password) 
        user.save(using = self._db)
        return user
    def create_superuser(self, email, username=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, username, password, **extra_fields)
    
class Provider_register(AbstractUser):
    name = models.CharField(max_length=50)
    email=models.EmailField(max_length=30,unique=True)
    username=models.CharField(max_length=30,unique=True)
    phone_number =models.BigIntegerField(blank=True, null=True)
    date_of_birth =models.DateField( blank=True, null=True)
    gender =models.CharField(max_length=10 ,blank=True, null=True)
    bank_number = models.CharField(max_length=20,blank=True, null=True)
    profile = models.ImageField()

    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default = False)

    objects = customUserManager()


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email
        




class Register_form(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    mobile = models.BigIntegerField()
    age = models.IntegerField()
    passewrd = models.CharField( max_length=16)
    passewrd1 = models.CharField(max_length=16)
    
    
class cntact_us(models.Model):
    emai_id=models.EmailField(max_length=30)
    messages = models.CharField(max_length=200)
    
    
    
class Addvaickal(models.Model):
    
    Vai_name  = models.CharField(max_length=50)
    RC = models.FileField()
    cost = models.IntegerField()
    vai_number = models.CharField(max_length=50)
    cost_per_hr = models.IntegerField()
    image = models.ImageField()
    
class vaik_taking_user(models.Model):
    name = models.CharField(max_length=50)
    Phone_valid = models.BigIntegerField()
    licence = models.FileField()
    taker_img =  models.ImageField()
    time_to_take_days =  models.IntegerField()
    time_in_hr = models.IntegerField()
    

