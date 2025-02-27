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

class Contact(models.Model):
    address = models.CharField(max_length=255)  # Andijan, Uzbekistan
    email = models.EmailField()  # alihadid@gmail.com
    phone = models.CharField(max_length=20)  # 88 972 10 03
    birth_date = models.DateField()  # 2nd August 1999
    
    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"
    
    def save(self, *args, **kwargs):
        if Contact.objects.exists() and not self.pk:
            raise ValidationError('Faqat bitta Contact yaratish mumkin')
        return super().save(*args, **kwargs)
    
    def __str__(self):
        return self.email 

class SkillCategory(models.Model):
    name = models.CharField(max_length=100)  # Modeling, Programming, Design etc.
    icon = models.ImageField(upload_to='categories/', null=True, blank=True)
    
    class Meta:
        verbose_name = "Skill Category"
        verbose_name_plural = "Skill Categories"
    
    def __str__(self):
        return self.name

class TechnicalSkill(models.Model):
    name = models.CharField(max_length=100)  # Revit, Python, Photoshop etc.
    category = models.ForeignKey(SkillCategory, on_delete=models.CASCADE, related_name='skills')
    icon = models.ImageField(upload_to='skills/')
    proficiency = models.IntegerField(default=0, help_text="Skill darajasi (0-100)")
    
    def __str__(self):
        return f"{self.name} ({self.category.name})"

class Hobby(models.Model):
    name = models.CharField(max_length=100)  # masalan: "Listening to music"
    icon = models.ImageField(upload_to='hobbies/')
    
    class Meta:
        verbose_name_plural = "Hobbies"
    
    def __str__(self):
        return self.name

class Language(models.Model):
    LEVEL_CHOICES = (
        ('native', 'Native'),
        ('basic', 'Basic'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
        ('fluent', 'Fluent'),
    )
    
    name = models.CharField(max_length=50)  # masalan: "Uzbek"
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES)
    
    def __str__(self):
        return f"{self.name} ({self.level})" 