from django.core.exceptions import ValidationError
from django.db import models

class PersonalInfo(models.Model):
    full_name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    bio = models.TextField()
    profile_image = models.ImageField(upload_to='profile/')
    email = models.EmailField()
    
    class Meta:
        verbose_name = "Personal info"
    
    def save(self, *args, **kwargs):
        if PersonalInfo.objects.exists() and not self.pk:
            raise ValidationError('Faqat bitta PersonalInfo yaratish mumkin')
        return super().save(*args, **kwargs)
    
    def __str__(self):
        return self.full_name

class Education(models.Model):
    year_start = models.CharField(max_length=4)
    year_end = models.CharField(max_length=4)
    institution = models.CharField(max_length=255)
    degree = models.CharField(max_length=255)
    
class Experience(models.Model):
    year_start = models.CharField(max_length=4)
    year_end = models.CharField(max_length=4)
    company = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    description = models.TextField() 

class Project(models.Model):
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    tools = models.ManyToManyField('Tool')
    
class Tool(models.Model):
    name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='tools/') 

class SocialLink(models.Model):
    platform = models.CharField(max_length=50)
    username = models.CharField(max_length=100)
    url = models.URLField() 