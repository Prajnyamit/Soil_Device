from django.db import models
from django.contrib.auth.hashers import make_password,check_password

class User(models.Model):

    name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=20,null=True,blank=True)
    last_name = models.CharField(max_length=20,null=True,blank=True)
    email = models.EmailField(unique=True)
    number = models.CharField(max_length=13,unique=True)
    password = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_superuser=models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        db_table = "users"

    def set_password(self,raw_password):
        self.password=make_password(raw_password)

    def check_password(self,raw_password):
        return check_password(raw_password,self.password)
    
    @property
    def is_authenticated(self):
        return True

    def __str__(self):
        return self.name