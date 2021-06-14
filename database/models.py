from django.db import models

# Create your models here.
class userlist(models.Model):
    name = models.CharField('Full Name', max_length=50, null=False)
    gender = models.CharField('Gender', max_length=6, null=False)
    dob = models.DateField('Date Of Birth')
    contact = models.CharField('Contact Number', max_length=10, null=False)
    country = models.CharField('Country Of Residence', max_length=50, null=False)
    email = models.EmailField('Email Address', max_length=254, null=False, primary_key=True)
    password = models.CharField('Password', max_length=50, null=False)
