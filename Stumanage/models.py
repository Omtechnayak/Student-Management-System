from django.db import models

# Create your models here.

class Students(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    email = models.EmailField()
    profilePic = models.ImageField(upload_to="profile_pic/",null=True,blank=True)
    resume = models.FileField(upload_to="resume/",null=True,blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
    




