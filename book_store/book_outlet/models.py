from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=40)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])
    author = models.CharField(max_length=40)
    is_bestselling = models.BooleanField()
    
    def __str__(self):
        return f"{self.title} ({self.rating})"