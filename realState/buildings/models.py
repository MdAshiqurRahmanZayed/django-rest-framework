from django.db import models
from django.db.models.deletion import DO_NOTHING
from django.utils.timezone import now
from realtor.models import Agent
from PIL import Image
from django.utils.crypto import get_random_string
from django.utils.text import slugify

def unique_slugify(instance, slug):
    model = instance.__class__
    unique_slug = slug
    while model.objects.filter(slug=unique_slug).exists():
        unique_slug = slug + get_random_string(length=5)
    return unique_slug


class Home(models.Model):
    class SaleType(models.TextChoices):
        FOR_SALE='For Sale'
        FOR_RENT='For Rent'
    class HomeType(models.TextChoices):
        HOUSE='House'
        FLAT='Flat'
        TOWNHOUSE='Townhouse'
    agent=models.ForeignKey(Agent, on_delete=DO_NOTHING, related_name='agents')
    slug=models.CharField(max_length=200,unique=True)
    title=models.CharField(max_length=150,unique=True)
    address=models.CharField(max_length=150)
    city=models.CharField(max_length=150)
    state=models.CharField(max_length=150)
    zipcode=models.CharField(max_length=150)
    description=models.TextField(blank=True)
    sale_type=models.CharField(max_length=50,choices=SaleType.choices, default=SaleType.FOR_SALE)
    home_type=models.CharField(max_length=50,choices=HomeType.choices, default=HomeType.HOUSE)
    price=models.IntegerField()
    bedrooms=models.IntegerField()
    bathrooms=models.IntegerField()
    sqft=models.IntegerField()
    open_house=models.BooleanField(default=False)
    photo=models.ImageField(upload_to='home',blank=True)
    is_published=models.BooleanField(default=True)
    list_date=models.DateTimeField(default=now,blank=True)
    created_at = models.DateTimeField(auto_now_add = True) 
    modified_at = models.DateTimeField(auto_now = True)   
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = unique_slugify(self, slugify(self.title))
        super().save(*args, **kwargs)
        
        
    def __str__(self):
        return self.slug 
    
    
class ImageFiles(models.Model):
    image = models.ImageField(upload_to="home")
    home = models.ForeignKey(
        Home, on_delete=models.CASCADE, related_name='images')
    created_at = models.DateTimeField(auto_now_add = True) 
    modified_at = models.DateTimeField(auto_now = True) 
    def save( self, *args, **kwargs):
        super(ImageFiles, self).save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300 :
            output_size =(300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
            
    def __str__(self):
        return self.home.title