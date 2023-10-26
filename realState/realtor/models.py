from django.db import models


class Agent(models.Model):
     name = models.CharField( max_length=50)
     biodata = models.TextField()
     email = models.EmailField(max_length=254)
     phone = models.CharField( max_length=17)
     image = models.ImageField( upload_to='realtor',null=True,blank=True)
     top_seller = models.BooleanField(default=False)
     date_hired = models.DateField(auto_now_add=True)
     
     def __str__(self):
          return self.name 