from django.db import models
from django.utils import timezone


class Category(models.Model):
    title = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.title}"


class Notes(models.Model):
    title = models.CharField(max_length=500)
    text = models.CharField(max_length=500)
    reminder = models.DateTimeField(default=timezone.now)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category', default=1)

    def __str__(self):
        return f"{self.title}"





