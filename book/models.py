from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=300, blank=True, null=True)
    slug = models.SlugField(max_length=300)
    author = models.CharField(max_length=200, blank=True, null=True)
    genre = models.CharField(max_length=150, blank=True, null=True)
    rating = models.FloatField(default=1, validators=[MinValueValidator(1), MaxValueValidator(5)])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Book, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} wrote by {self.author}"


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_review')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='book_review')
    review_text = models.TextField(blank=True, null=True)
    rating = models.FloatField(default=1, validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return f"{self.user.username} review {self.book.title}"
