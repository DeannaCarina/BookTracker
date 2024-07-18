from django.contrib.auth.models import User
from django.conf import settings
from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator

class Book(models.Model):
    #The default behavior for Django Models is to create an auto-incrementing integer primary key with the name “id”. 
    #If there is not a field defined with the attribute primary_key=True, Django will add it to the model automatically.
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    published = models.IntegerField(validators=[MinValueValidator(1000), MaxValueValidator(3000)])
    pages = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100000)])
    progress = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100000)])
    frontcover = models.ImageField(null=True, blank=True, upload_to='frontcovers') 
    genre = models.TextField(max_length=2550)
    keypoints = models.TextField(blank=True, max_length=25500)

    def __str__(self):
        return self.title
    
    @property
    def Get_calculation(self):
        get_calculation = (self.progress/self.pages)*100
        return get_calculation