from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    username = models.CharField(verbose_name='Enter Email address or username', max_length=150,unique=True)
    email = models.EmailField(verbose_name='Email address',unique=True,null=False,blank=False)
    # USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = []
    
    def save(self, *args, **kwargs):
        print(self.email,self.username) 
        if not self.username:
            username = self.email.split('@')[0] + '_' + self.email.split('@')[1].split('.')[0]
            self.username = username
        super().save(*args, **kwargs)
    