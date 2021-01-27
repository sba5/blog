from django.db import models
from django import forms
# Create your models here.

class Members(models.Model):
    id = models.AutoField(primary_key=True)
    userid = models.CharField(max_length=16, verbose_name="user_id")
    #userpassword = forms.CharField(widget=forms.PasswordInput)
    userpassword = models.CharField(max_length=16, verbose_name="user_password",null=True, default='')
    username = models.CharField(max_length=16, verbose_name="user_name",null=True)
    usergender = models.CharField(max_length=2,verbose_name="user_gender",null=True, default='')
    useremail = models.EmailField(max_length=128, verbose_name="user_email")
    userphone = models.CharField(max_length=16, verbose_name="user_phone")
    useraddress = models.CharField(max_length=128, verbose_name="user_address", null=True, default='')

    created = models.DateTimeField(auto_now_add=True, verbose_name="register_time")
    update = models.DateTimeField(auto_now_add=True, verbose_name="modify_time")
    
    class Meta:
        db_table = "world_users"
        verbose_name = "World_Users"
        verbose_name_plural = "World Users"

    def __str__(self):
        return self.username
