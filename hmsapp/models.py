from django.db import models

# Create your models here.
class staff(models.Model):
    Maleorfemale=[('male', 'Male'), ('female', 'Female')]
    
    firstname = models.CharField(max_length=30,null=True)
    lastname = models.CharField(max_length=30,null=True)
    username = models.CharField(max_length=30,null=True)
    email = models.CharField(max_length=50,null=True)
    phone = models.CharField(max_length=20,null=True)
    gender = models.CharField(max_length=10, choices=Maleorfemale)
    password = models.CharField(max_length=100,null=True)
    confirm_password = models.CharField(max_length=100,null=True)

   
    
    def __str__(self):
        return self.username
    

class customer(models.Model):
    Maleorfemale=[('male', 'Male'), ('female', 'Female')]
    
    firstname = models.CharField(max_length=30,null=True)
    lastname = models.CharField(max_length=30,null=True)
    username = models.CharField(max_length=30,null=True)
    email = models.CharField(max_length=50,null=True)
    phone = models.CharField(max_length=20,null=True)
    gender = models.CharField(max_length=10, choices=Maleorfemale)
    password = models.CharField(max_length=100,null=True)
    confirm_password = models.CharField(max_length=100,null=True)
   
    


   
    
    def __str__(self):
        return self.username    
    



class room(models.Model):
     no = models.CharField(max_length=30,null=True)
     roomtype = models.CharField(max_length=30,null=True)
     price = models.CharField(max_length=30,null=True)
     availability=models.BooleanField(default=False)
   
    


   
    
      