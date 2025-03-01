from django.contrib.auth.backends import BaseBackend
from .models import Provider_register

from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django import forms

CHOICES = [
    ('Male', 'Male'),
    ('Female', 'Female'),
]

class customusercreationform(UserCreationForm):

    name = forms.CharField(max_length=100,
                                 required=True,
                                 widget=forms.TextInput(attrs={'placeholder': 'Enter Your Full Name',
                                                                'class':'mt-2 bg-transparent w-[197px] px-4 py-4 border-2 border-gray-500 round-lg'
                                                               }))
    email = forms.EmailField(max_length=100,
                                required=True,
                                widget=forms.TextInput(attrs={'placeholder': 'Email Id',
                                                              'class':'mt-2 bg-transparent w-[197px] px-4 py-4 border-2 border-gray-500 round-lg'
                                                              }))
    username= forms.CharField(max_length=100,
                                required=True,
                                widget=forms.TextInput(attrs={'placeholder': 'Last Name',
                                                              'class':'mt-2 bg-transparent w-[197px] px-4 py-4 border-2 border-gray-500 round-lg'
                                                              }))


    phone_number= forms.CharField(max_length=50,
                                required=True,
                                widget=forms.TextInput(attrs={'placeholder': ' Phone Number',
                                                              'class':'mt-2 bg-transparent w-[197px] px-4 py-4 border-2 border-gray-500 round-lg'
                                                              }))
    gender= forms.ChoiceField( choices=CHOICES,
                                required=False,
                                label="Choose your Gender",
                                widget=forms.RadioSelect(attrs={'class':'calume text-center'}))
    date_of_birth= forms.DateField(
                                required=True,
                                widget=forms.TextInput(attrs={'placeholder': ' Date of Birth',
                                                              'class':'mt-2 bg-transparent w-[197px] px-4 py-4 border-2 border-gray-500 round-lg'
                                                              }))
    
    bank_number= forms.IntegerField(
                                required=True,
                                widget=forms.TextInput(attrs={'placeholder': ' Bank Account Number',
                                                              'class':'mt-2 bg-transparent w-[197px] px-4 py-4 border-2 border-gray-500 round-lg'
                                                              }))
    profile= forms.ImageField(required=False)
    class Meta:
        model = Provider_register
        fields = ('name', 'username','email','password1', 'password2','phone_number','gender','date_of_birth','bank_number','profile')

    def __init__(self, *args, **kwargs):
        super(customusercreationform, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


'''
class LoginForm(AuthenticationForm):
    email = forms.EmailField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'email',
                                                             'class': 'form-control',
                                                             }))
    password = forms.CharField(max_length=50,
                               required=True,
                               widget=forms.PasswordInput(attrs={'placeholder': 'Password',
                                                                 'class': 'form-control',
                                                                 'data-toggle': 'password',
                                                                 'id': 'password',
                                                                 'name': 'password',
                                                                 }))
#   remember_me = forms.BooleanField(required=False)

    class Meta:
        model = Provider_register
        fields = ['email', 'password']
'''     


'''
from django.db import models
from django.contrib.auth.models import BaseUserManager , AbstractBaseUser , PermissionsMixin,AbstractUser

class customUserManager(BaseUserManager):
    def create_user(self,email,password=None,**extra_fields):
        if not email:
            raise ValueError('You did not entered a valid email')
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using = self._db)
        return user
    
    
    def create_superuser(self, email,password=None, **extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)

        return self.create_user(email,password,**extra_fields)
                      
class customuser(AbstractBaseUser,PermissionsMixin):

    first_name = models.CharField(max_length=50,blank = True)
    last_name =  models.CharField(max_length=50,blank = True)
    username  = models.CharField(max_length=50,blank = True)
    email = models.CharField(max_length=50,blank = True,unique=True)
    
    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default = False)

    objects = customUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
'''

