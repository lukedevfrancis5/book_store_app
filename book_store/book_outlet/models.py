from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=40)
    rating = models.IntegerField(
        default = 1,
        validators= [
            MaxValueValidator(10),
            MinValueValidator(1)
        ]
    )
    