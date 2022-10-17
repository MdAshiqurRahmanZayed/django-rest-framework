from django.db import models

# Create your models here.
class ToDo(models.Model):
     title = models.CharField( max_length=50)
     discription = models.TextField()
     completed = models.BooleanField(default = False,blank=True,null=True)

    

     class Meta:
          verbose_name = ("ToDo")
          verbose_name_plural = ("ToDos")

     def __str__(self):
          return self.title

#     def get_absolute_url(self):
#         return reverse("ToDo_detail", kwargs={"pk": self.pk})
