
from django.db import models

from django.core.validators import RegexValidator
from django.core.validators import validate_email


# validate_email("name@mail.56") to validate email

# Create your models here.

class users_new(models.Model):
    userId= models.AutoField(primary_key=True)
    name= models.CharField(max_length=20, error_messages={'required': 'Please enter name.'})
    mobilenumber= models.CharField(max_length=10 ,unique=True, error_messages={'required': 'Please enter mobile number',"unique" :"This mobile number is already "
                                                                                       "registered. Please login or enter different mobile number "})
                 # RegexField(regex=r'^\+?1?\d{9,15}$', error_message = ("Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")                                                                     "use different number."})
    password= models.CharField(max_length=80, blank=False, error_messages={'required': 'Password cannot be null'})
    emailid= models.EmailField(max_length=50, blank=False, unique=True,error_messages={'required': 'Please provide your email address.',
                                                                                        'unique': 'An account with this email exists.'})
   # phone= models.RegexValidator(regex = r'^\+?1?\d{9,15}$',message = "Phone number must be enter of 10 digits")
    # acc_created= models.CharField(max_length=20,blank=True,null=True)
    #mobilenumber= models.RegexField(required=True,max_length=10 ,unique=True,regex=r'^\+?1?\d{9,15}$',
                                #error_message = ("Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."))
    #friendslist= models.CharField(max_length=20 ,blank=True ,null=True)
    otp = models.CharField(max_length=4, null=False, blank=False)
    acc_created = models.DateTimeField(auto_now=True)
    private= models.BooleanField(default=False,blank=False,error_messages={"blank":"Please choose public or private","null":"make private or public check!!"})
    twoFA = models.BooleanField(default=False,blank=False,error_messages={"blank":"Please choose public or private","null":"make private or public check!!"})

    # class Meta:
      #  db_table= 'mydb'
