from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse 
from django.utils.text import slugify
# Create your models here.

# Book class with attributes

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)


class Book(models.Model):
    title = models.CharField(max_length=40)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    is_bestselling = models.BooleanField(default=False)
    slug = models.SlugField(default="", blank=True, null=False, db_index=True) # Harry Potter 1 => harry-potter-1

    def get_absolute_url(self):
        return reverse("book-detail", args=[self.slug])

    def __str__(self):
        return f"{self.title} ({self.rating})"
    
